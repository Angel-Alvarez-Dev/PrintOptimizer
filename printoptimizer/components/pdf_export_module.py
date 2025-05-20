import reflex as rx
from printoptimizer.states.print_optimizer_state import (
    PrintOptimizerState,
)


def pdf_export_module() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "PDF Export Module",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "text-xl font-semibold text-[#F5F5F5] mb-4",
                "text-xl font-semibold text-black mb-4",
            ),
        ),
        rx.el.p(
            "Select a report template and export data as PDF.",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "text-[#A0A0A0] mb-4",
                "text-gray-600 mb-4",
            ),
        ),
        rx.el.select(
            rx.el.option(
                "Profitability Report (Project)",
                value="profit_project",
            ),
            rx.el.option(
                "Performance Report (Design)",
                value="perf_design",
            ),
            rx.el.option(
                "Consolidated Monthly Report",
                value="monthly_consolidated",
            ),
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "w-full p-2 mb-4 bg-[#2a2a2a] text-[#F5F5F5] border border-[#333333] rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
                "w-full p-2 mb-4 bg-white text-black border border-gray-300 rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
            ),
        ),
        rx.el.button(
            "Export PDF",
            on_click=PrintOptimizerState.export_pdf_report,
            class_name="w-full p-2 bg-[#E63946] text-[#F5F5F5] rounded-md hover:bg-opacity-80 transition-colors",
        ),
        class_name=rx.cond(
            PrintOptimizerState.theme == "dark",
            "mt-8 p-4 bg-[#252525] rounded-lg shadow-md",
            "mt-8 p-4 bg-white rounded-lg shadow-md border border-gray-200",
        ),
    )