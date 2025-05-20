import reflex as rx
from printoptimizer.states.print_optimizer_state import (
    PrintOptimizerState,
    CostItem,
)


def cost_item_row(item: CostItem) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            item["name"],
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "py-2 px-4 text-[#F5F5F5]",
                "py-2 px-4 text-black",
            ),
        ),
        rx.el.td(
            rx.el.div(
                rx.el.span(
                    "$",
                    class_name=rx.cond(
                        PrintOptimizerState.theme == "dark",
                        "mr-1 text-[#A0A0A0]",
                        "mr-1 text-gray-600",
                    ),
                ),
                rx.el.input(
                    default_value=item[
                        "cost_per_unit"
                    ].to_string(),
                    on_change=lambda val: PrintOptimizerState.update_cost_item_cost_per_unit(
                        item["name"], val
                    ),
                    type="number",
                    step="0.01",
                    min="0",
                    class_name=rx.cond(
                        PrintOptimizerState.theme == "dark",
                        "w-24 p-1 bg-[#2a2a2a] text-[#F5F5F5] border border-[#333333] rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
                        "w-24 p-1 bg-white text-black border border-gray-300 rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
                    ),
                ),
                rx.el.span(
                    item["unit"],
                    class_name=rx.cond(
                        PrintOptimizerState.theme == "dark",
                        "ml-2 text-[#A0A0A0]",
                        "ml-2 text-gray-600",
                    ),
                ),
                class_name="flex items-center",
            ),
            class_name="py-2 px-4",
        ),
        rx.el.td(
            rx.el.div(
                rx.el.input(
                    default_value=item[
                        "quantity"
                    ].to_string(),
                    on_change=lambda val: PrintOptimizerState.update_cost_item_quantity(
                        item["name"], val
                    ),
                    type="number",
                    step="0.01",
                    min="0",
                    class_name=rx.cond(
                        PrintOptimizerState.theme == "dark",
                        "w-20 p-1 bg-[#2a2a2a] text-[#F5F5F5] border border-[#333333] rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
                        "w-20 p-1 bg-white text-black border border-gray-300 rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
                    ),
                ),
                class_name="flex items-center",
            ),
            class_name="py-2 px-4",
        ),
        rx.el.td(
            item["file_type"],
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "py-2 px-4 text-[#F5F5F5]",
                "py-2 px-4 text-black",
            ),
        ),
        rx.el.td(
            item["client_project_name"],
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "py-2 px-4 text-[#F5F5F5]",
                "py-2 px-4 text-black",
            ),
        ),
        rx.el.td(
            f"${item['cost_per_unit'] * item['quantity']:.2f}",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "py-2 px-4 text-[#F5F5F5] text-right",
                "py-2 px-4 text-black text-right",
            ),
        ),
    )


def cost_control_panel() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2(
                "Cost Control Panel",
                class_name=rx.cond(
                    PrintOptimizerState.theme == "dark",
                    "text-xl font-semibold text-[#F5F5F5]",
                    "text-xl font-semibold text-black",
                ),
            ),
            rx.el.div(
                rx.el.button(
                    "Download PDF",
                    on_click=PrintOptimizerState.export_cost_control_pdf,
                    class_name="p-1 px-2 text-sm bg-[#E63946] text-[#F5F5F5] rounded-md hover:bg-opacity-80 transition-colors mr-2",
                ),
                rx.el.button(
                    rx.icon(
                        tag=rx.cond(
                            PrintOptimizerState.cost_control_expanded,
                            "chevron-up",
                            "chevron-down",
                        )
                    ),
                    on_click=PrintOptimizerState.toggle_cost_control_expansion,
                    class_name=rx.cond(
                        PrintOptimizerState.theme == "dark",
                        "p-1 text-[#A0A0A0] hover:text-[#F5F5F5]",
                        "p-1 text-gray-600 hover:text-black",
                    ),
                ),
                class_name="flex items-center",
            ),
            class_name="flex justify-between items-center mb-4",
        ),
        rx.cond(
            PrintOptimizerState.cost_control_expanded,
            rx.el.div(
                rx.el.table(
                    rx.el.thead(
                        rx.el.tr(
                            rx.el.th(
                                "Item",
                                class_name=rx.cond(
                                    PrintOptimizerState.theme
                                    == "dark",
                                    "py-2 px-4 text-left text-sm font-medium text-[#A0A0A0] uppercase",
                                    "py-2 px-4 text-left text-sm font-medium text-gray-500 uppercase",
                                ),
                            ),
                            rx.el.th(
                                "Cost Per Unit",
                                class_name=rx.cond(
                                    PrintOptimizerState.theme
                                    == "dark",
                                    "py-2 px-4 text-left text-sm font-medium text-[#A0A0A0] uppercase",
                                    "py-2 px-4 text-left text-sm font-medium text-gray-500 uppercase",
                                ),
                            ),
                            rx.el.th(
                                "Quantity",
                                class_name=rx.cond(
                                    PrintOptimizerState.theme
                                    == "dark",
                                    "py-2 px-4 text-left text-sm font-medium text-[#A0A0A0] uppercase",
                                    "py-2 px-4 text-left text-sm font-medium text-gray-500 uppercase",
                                ),
                            ),
                            rx.el.th(
                                "File Type",
                                class_name=rx.cond(
                                    PrintOptimizerState.theme
                                    == "dark",
                                    "py-2 px-4 text-left text-sm font-medium text-[#A0A0A0] uppercase",
                                    "py-2 px-4 text-left text-sm font-medium text-gray-500 uppercase",
                                ),
                            ),
                            rx.el.th(
                                "Client/Project",
                                class_name=rx.cond(
                                    PrintOptimizerState.theme
                                    == "dark",
                                    "py-2 px-4 text-left text-sm font-medium text-[#A0A0A0] uppercase",
                                    "py-2 px-4 text-left text-sm font-medium text-gray-500 uppercase",
                                ),
                            ),
                            rx.el.th(
                                "Total Cost",
                                class_name=rx.cond(
                                    PrintOptimizerState.theme
                                    == "dark",
                                    "py-2 px-4 text-right text-sm font-medium text-[#A0A0A0] uppercase",
                                    "py-2 px-4 text-right text-sm font-medium text-gray-500 uppercase",
                                ),
                            ),
                        )
                    ),
                    rx.el.tbody(
                        rx.foreach(
                            PrintOptimizerState.cost_control_data,
                            cost_item_row,
                        ),
                        rx.el.tr(
                            rx.el.td(
                                "Total Overall",
                                class_name=rx.cond(
                                    PrintOptimizerState.theme
                                    == "dark",
                                    "py-2 px-4 font-bold text-[#F5F5F5]",
                                    "py-2 px-4 font-bold text-black",
                                ),
                                col_span=5,
                            ),
                            rx.el.td(
                                f"${PrintOptimizerState.total_cost_control_value:.2f}",
                                class_name=rx.cond(
                                    PrintOptimizerState.theme
                                    == "dark",
                                    "py-2 px-4 font-bold text-[#F5F5F5] text-right",
                                    "py-2 px-4 font-bold text-black text-right",
                                ),
                            ),
                        ),
                    ),
                    class_name="w-full",
                ),
                class_name=rx.cond(
                    PrintOptimizerState.theme == "dark",
                    "p-4 bg-[#252525] rounded-lg shadow-md",
                    "p-4 bg-white rounded-lg shadow-md border border-gray-200",
                ),
            ),
        ),
        class_name="mt-8",
    )