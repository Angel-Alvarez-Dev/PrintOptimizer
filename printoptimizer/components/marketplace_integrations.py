import reflex as rx
from printoptimizer.states.print_optimizer_state import (
    PrintOptimizerState,
    MarketplaceStats,
    DesignEntry,
    MarketplaceName,
)
from typing import get_args


def marketplace_card(
    stats: MarketplaceStats,
) -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            stats["name"],
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "text-lg font-semibold text-[#F5F5F5] mb-2",
                "text-lg font-semibold text-black mb-2",
            ),
        ),
        rx.el.p(
            f"Views: {stats['views']}",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "text-sm text-[#A0A0A0]",
                "text-sm text-gray-600",
            ),
        ),
        rx.el.p(
            f"Downloads: {stats['downloads']}",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "text-sm text-[#A0A0A0]",
                "text-sm text-gray-600",
            ),
        ),
        rx.cond(
            stats["pledges"] != None,
            rx.el.p(
                f"Pledges: {stats['pledges']}",
                class_name=rx.cond(
                    PrintOptimizerState.theme == "dark",
                    "text-sm text-[#A0A0A0]",
                    "text-sm text-gray-600",
                ),
            ),
            rx.fragment(),
        ),
        rx.el.p(
            f"Revenue: ${stats['revenue']:.2f}",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "text-sm text-[#A0A0A0]",
                "text-sm text-gray-600",
            ),
        ),
        rx.el.p(
            f"Payments: {stats['payment_methods'].join(', ')}",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "text-sm text-[#A0A0A0] mt-1",
                "text-sm text-gray-600 mt-1",
            ),
        ),
        class_name=rx.cond(
            PrintOptimizerState.theme == "dark",
            "p-4 bg-[#252525] rounded-lg shadow-md",
            "p-4 bg-white rounded-lg shadow-md border border-gray-200",
        ),
    )


def manual_design_card(design: DesignEntry) -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            design["name"],
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "text-lg font-semibold text-[#F5F5F5] mb-2",
                "text-lg font-semibold text-black mb-2",
            ),
        ),
        rx.el.p(
            design["description"],
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "text-sm text-[#A0A0A0]",
                "text-sm text-gray-600",
            ),
        ),
        rx.el.p(
            f"Platform: {design['platform']}",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "text-xs text-[#A0A0A0] mt-1",
                "text-xs text-gray-600 mt-1",
            ),
        ),
        rx.cond(
            design["file_path"] != None,
            rx.el.p(
                f"File: {design['file_path']}",
                class_name=rx.cond(
                    PrintOptimizerState.theme == "dark",
                    "text-xs text-[#A0A0A0]",
                    "text-xs text-gray-600",
                ),
            ),
            rx.fragment(),
        ),
        class_name=rx.cond(
            PrintOptimizerState.theme == "dark",
            "p-4 bg-[#2a2a2a] rounded-lg shadow-md",
            "p-4 bg-white rounded-lg shadow-md border border-gray-200",
        ),
    )


def add_design_form() -> rx.Component:
    return rx.el.form(
        rx.el.h3(
            "Add New Manual Design",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "text-lg font-semibold text-[#F5F5F5] mb-3",
                "text-lg font-semibold text-black mb-3",
            ),
        ),
        rx.el.label(
            "Design Name:",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "block text-sm font-medium text-[#A0A0A0] mb-1",
                "block text-sm font-medium text-gray-700 mb-1",
            ),
        ),
        rx.el.input(
            name="name",
            placeholder="Enter design name",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "w-full p-2 mb-3 bg-[#2a2a2a] text-[#F5F5F5] border border-[#333333] rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
                "w-full p-2 mb-3 bg-white text-black border border-gray-300 rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
            ),
        ),
        rx.el.label(
            "Description:",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "block text-sm font-medium text-[#A0A0A0] mb-1",
                "block text-sm font-medium text-gray-700 mb-1",
            ),
        ),
        rx.el.textarea(
            name="description",
            placeholder="Enter design description",
            rows=3,
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "w-full p-2 mb-3 bg-[#2a2a2a] text-[#F5F5F5] border border-[#333333] rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
                "w-full p-2 mb-3 bg-white text-black border border-gray-300 rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
            ),
        ),
        rx.el.div(
            rx.el.button(
                "Cancel",
                type="button",
                on_click=PrintOptimizerState.toggle_add_design_form,
                class_name=rx.cond(
                    PrintOptimizerState.theme == "dark",
                    "p-2 bg-gray-600 text-[#F5F5F5] rounded-md hover:bg-gray-500 transition-colors",
                    "p-2 bg-gray-300 text-black rounded-md hover:bg-gray-400 transition-colors",
                ),
            ),
            rx.el.button(
                "Add Design",
                type="submit",
                class_name="p-2 bg-[#E63946] text-[#F5F5F5] rounded-md hover:bg-opacity-80 transition-colors",
            ),
            class_name="flex justify-end space-x-2 mt-2",
        ),
        on_submit=PrintOptimizerState.add_manual_design,
        reset_on_submit=True,
        class_name=rx.cond(
            PrintOptimizerState.theme == "dark",
            "p-4 bg-[#252525] rounded-lg shadow-md mb-6",
            "p-4 bg-white rounded-lg shadow-md mb-6 border border-gray-200",
        ),
    )


def marketplace_integrations() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2(
                "Marketplace Integrations",
                class_name=rx.cond(
                    PrintOptimizerState.theme == "dark",
                    "text-xl font-semibold text-[#F5F5F5]",
                    "text-xl font-semibold text-black",
                ),
            ),
            rx.el.button(
                rx.cond(
                    PrintOptimizerState.show_add_design_form,
                    "Close Form",
                    "Add Design Manually",
                ),
                on_click=PrintOptimizerState.toggle_add_design_form,
                class_name="p-2 bg-[#E63946] text-[#F5F5F5] rounded-md hover:bg-opacity-80 transition-colors",
            ),
            class_name="flex justify-between items-center mb-4",
        ),
        rx.cond(
            PrintOptimizerState.show_add_design_form,
            add_design_form(),
        ),
        rx.el.h3(
            "Automated Platform Stats",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "text-lg font-semibold text-[#F5F5F5] mb-3 mt-6",
                "text-lg font-semibold text-black mb-3 mt-6",
            ),
        ),
        rx.el.div(
            rx.foreach(
                PrintOptimizerState.marketplace_data,
                marketplace_card,
            ),
            class_name="grid grid-cols-1 md:grid-cols-2 gap-6",
        ),
        rx.el.h3(
            "Manually Added Designs",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "text-lg font-semibold text-[#F5F5F5] mb-3 mt-8",
                "text-lg font-semibold text-black mb-3 mt-8",
            ),
        ),
        rx.cond(
            PrintOptimizerState.manually_added_designs.length()
            == 0,
            rx.el.p(
                "No manual designs added yet.",
                class_name=rx.cond(
                    PrintOptimizerState.theme == "dark",
                    "text-[#A0A0A0] text-center py-4",
                    "text-gray-500 text-center py-4",
                ),
            ),
            rx.el.div(
                rx.foreach(
                    PrintOptimizerState.manually_added_designs,
                    manual_design_card,
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 gap-6",
            ),
        ),
        class_name="mt-8",
    )