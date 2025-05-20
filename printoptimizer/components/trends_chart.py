import reflex as rx
from printoptimizer.states.print_optimizer_state import (
    PrintOptimizerState,
)


def trends_chart() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "Performance Trends",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "text-xl font-semibold text-[#F5F5F5] mb-4",
                "text-xl font-semibold text-black mb-4",
            ),
        ),
        rx.el.div(
            rx.el.select(
                rx.foreach(
                    [
                        "All Platforms",
                        "Thingiverse",
                        "MyMiniFactory",
                        "Cults3D",
                        "Patreon",
                    ],
                    lambda opt: rx.el.option(
                        opt,
                        value=opt.lower().replace(" ", "_"),
                    ),
                ),
                default_value=PrintOptimizerState.selected_trend_platform,
                class_name=rx.cond(
                    PrintOptimizerState.theme == "dark",
                    "bg-[#2a2a2a] text-[#F5F5F5] p-2 rounded-md border border-[#333333] focus:ring-[#E63946] focus:border-[#E63946]",
                    "bg-white text-black p-2 rounded-md border border-gray-300 focus:ring-[#E63946] focus:border-[#E63946]",
                ),
            ),
            rx.el.select(
                rx.foreach(
                    [
                        "Last 7 Days",
                        "Last 30 Days",
                        "Last 90 Days",
                        "All Time",
                    ],
                    lambda opt: rx.el.option(
                        opt,
                        value=opt.lower().replace(" ", "_"),
                    ),
                ),
                default_value=PrintOptimizerState.selected_trend_date_range,
                class_name=rx.cond(
                    PrintOptimizerState.theme == "dark",
                    "bg-[#2a2a2a] text-[#F5F5F5] p-2 rounded-md border border-[#333333] focus:ring-[#E63946] focus:border-[#E63946]",
                    "bg-white text-black p-2 rounded-md border border-gray-300 focus:ring-[#E63946] focus:border-[#E63946]",
                ),
            ),
            class_name="flex space-x-4 mb-4",
        ),
        rx.el.div(
            rx.recharts.responsive_container(
                rx.recharts.composed_chart(
                    rx.recharts.cartesian_grid(
                        stroke_dasharray="3 3",
                        stroke=rx.cond(
                            PrintOptimizerState.theme
                            == "dark",
                            "#333333",
                            "#e0e0e0",
                        ),
                    ),
                    rx.recharts.x_axis(
                        data_key="month",
                        stroke=rx.cond(
                            PrintOptimizerState.theme
                            == "dark",
                            "#A0A0A0",
                            "#505050",
                        ),
                    ),
                    rx.recharts.y_axis(
                        stroke=rx.cond(
                            PrintOptimizerState.theme
                            == "dark",
                            "#A0A0A0",
                            "#505050",
                        )
                    ),
                    rx.recharts.tooltip(
                        content_style=rx.cond(
                            PrintOptimizerState.theme
                            == "dark",
                            {
                                "background": "#252525",
                                "border": "1px solid #333333",
                            },
                            {
                                "background": "#ffffff",
                                "border": "1px solid #cccccc",
                            },
                        ),
                        item_style=rx.cond(
                            PrintOptimizerState.theme
                            == "dark",
                            {"color": "#F5F5F5"},
                            {"color": "#000000"},
                        ),
                        cursor={
                            "fill": "rgba(230, 57, 70, 0.1)"
                        },
                    ),
                    rx.recharts.legend(
                        wrapper_style=rx.cond(
                            PrintOptimizerState.theme
                            == "dark",
                            {"color": "#F5F5F5"},
                            {"color": "#000000"},
                        )
                    ),
                    rx.recharts.bar(
                        data_key="downloads",
                        fill=rx.cond(
                            PrintOptimizerState.theme
                            == "dark",
                            "#A0A0A0",
                            "#888888",
                        ),
                        name="Downloads",
                    ),
                    rx.recharts.line(
                        type="monotone",
                        data_key="sales",
                        stroke="#E63946",
                        name="Sales",
                        stroke_width=2,
                    ),
                    data=PrintOptimizerState.trends_chart_data,
                    on_mouse_move=PrintOptimizerState.handle_trend_chart_hover,
                ),
                height=300,
            ),
            rx.cond(
                PrintOptimizerState.hovered_trend_data,
                rx.el.div(
                    rx.el.p(
                        f"Month: {PrintOptimizerState.hovered_trend_data['month']}",
                        class_name=rx.cond(
                            PrintOptimizerState.theme
                            == "dark",
                            "text-sm text-[#F5F5F5]",
                            "text-sm text-black",
                        ),
                    ),
                    rx.el.p(
                        f"Sales: ${PrintOptimizerState.hovered_trend_data['sales']}",
                        class_name=rx.cond(
                            PrintOptimizerState.theme
                            == "dark",
                            "text-sm text-[#F5F5F5]",
                            "text-sm text-black",
                        ),
                    ),
                    rx.el.p(
                        f"Downloads: {PrintOptimizerState.hovered_trend_data['downloads']}",
                        class_name=rx.cond(
                            PrintOptimizerState.theme
                            == "dark",
                            "text-sm text-[#F5F5F5]",
                            "text-sm text-black",
                        ),
                    ),
                    class_name=rx.cond(
                        PrintOptimizerState.theme == "dark",
                        "mt-2 p-2 bg-[#2a2a2a] rounded",
                        "mt-2 p-2 bg-gray-100 rounded border border-gray-200",
                    ),
                ),
            ),
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "p-4 bg-[#252525] rounded-lg shadow-md",
                "p-4 bg-white rounded-lg shadow-md border border-gray-200",
            ),
        ),
        class_name="mt-8",
    )