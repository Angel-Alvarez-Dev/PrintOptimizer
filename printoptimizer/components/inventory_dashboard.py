import reflex as rx
from printoptimizer.states.print_optimizer_state import (
    PrintOptimizerState,
    InventoryItem,
)


def inventory_item_display(
    item: InventoryItem,
) -> rx.Component:
    is_low_stock = (
        item["stock_level"] <= item["low_stock_threshold"]
    )
    needs_reorder = (
        item["stock_level"] <= item["reorder_threshold"]
    )
    return rx.el.div(
        rx.el.h4(
            item["name"],
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "text-md font-semibold text-[#F5F5F5]",
                "text-md font-semibold text-black",
            ),
        ),
        rx.el.p(
            f"Stock: {item['stock_level']}{item['unit']}",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "text-sm text-[#A0A0A0]",
                "text-sm text-gray-600",
            ),
        ),
        rx.el.p(
            f"Low Stock At: {item['low_stock_threshold']}{item['unit']}",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "text-xs text-[#A0A0A0]",
                "text-xs text-gray-600",
            ),
        ),
        rx.el.p(
            f"Reorder At: {item['reorder_threshold']}{item['unit']}",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "text-xs text-[#A0A0A0]",
                "text-xs text-gray-600",
            ),
        ),
        rx.cond(
            needs_reorder,
            rx.el.span(
                "REORDER NOW",
                class_name="mt-2 inline-block px-2 py-0.5 text-xs rounded-full bg-red-700 text-white font-bold",
            ),
            rx.cond(
                is_low_stock,
                rx.el.span(
                    "Low Stock",
                    class_name="mt-2 inline-block px-2 py-0.5 text-xs rounded-full bg-yellow-600 text-white",
                ),
                rx.el.span(
                    "In Stock",
                    class_name="mt-2 inline-block px-2 py-0.5 text-xs rounded-full bg-green-600 text-white",
                ),
            ),
        ),
        class_name=rx.cond(
            PrintOptimizerState.theme == "dark",
            "p-4 bg-[#2a2a2a] rounded-md shadow",
            "p-4 bg-white rounded-md shadow border border-gray-200",
        ),
    )


def inventory_dashboard() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "Inventory Dashboard",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "text-xl font-semibold text-[#F5F5F5] mb-4",
                "text-xl font-semibold text-black mb-4",
            ),
        ),
        rx.el.div(
            rx.foreach(
                PrintOptimizerState.inventory_data,
                inventory_item_display,
            ),
            class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4",
        ),
        rx.cond(
            PrintOptimizerState.inventory_data.length()
            == 0,
            rx.el.p(
                "No inventory items tracked yet.",
                class_name=rx.cond(
                    PrintOptimizerState.theme == "dark",
                    "text-center text-[#A0A0A0] py-4",
                    "text-center text-gray-500 py-4",
                ),
            ),
        ),
        class_name="mt-8",
    )