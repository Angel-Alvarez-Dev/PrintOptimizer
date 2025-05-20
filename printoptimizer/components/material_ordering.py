import reflex as rx
from printoptimizer.states.print_optimizer_state import (
    PrintOptimizerState,
)


def material_ordering() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "Material Ordering (Placeholder)",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "text-xl font-semibold text-[#F5F5F5] mb-4",
                "text-xl font-semibold text-black mb-4",
            ),
        ),
        rx.el.p(
            "This section will allow placing and tracking purchase orders.",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "text-[#A0A0A0]",
                "text-gray-600",
            ),
        ),
        class_name=rx.cond(
            PrintOptimizerState.theme == "dark",
            "mt-8 p-4 bg-[#252525] rounded-lg shadow-md",
            "mt-8 p-4 bg-white rounded-lg shadow-md border border-gray-200",
        ),
    )