import reflex as rx
from printoptimizer.states.print_optimizer_state import (
    PrintOptimizerState,
)


def kpi_card(
    title: str,
    value: rx.Var[str | int | float],
    icon_name: str,
    value_prefix: str = "",
    value_suffix: str = "",
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(
                tag=icon_name,
                class_name="w-8 h-8 text-[#E63946]",
            ),
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "p-3 bg-[#2a2a2a] rounded-lg",
                "p-3 bg-gray-100 rounded-lg",
            ),
        ),
        rx.el.div(
            rx.el.p(
                title,
                class_name=rx.cond(
                    PrintOptimizerState.theme == "dark",
                    "text-sm font-medium text-[#A0A0A0]",
                    "text-sm font-medium text-gray-600",
                ),
            ),
            rx.el.p(
                f"{value_prefix}{value}{value_suffix}",
                class_name=rx.cond(
                    PrintOptimizerState.theme == "dark",
                    "text-2xl font-bold text-[#F5F5F5] mt-1",
                    "text-2xl font-bold text-black mt-1",
                ),
            ),
            class_name="ml-4",
        ),
        class_name=rx.cond(
            PrintOptimizerState.theme == "dark",
            "flex items-center p-4 bg-[#252525] rounded-lg shadow-md hover:shadow-lg transition-shadow",
            "flex items-center p-4 bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow border border-gray-200",
        ),
    )