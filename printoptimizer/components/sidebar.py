import reflex as rx
from printoptimizer.states.print_optimizer_state import (
    PrintOptimizerState,
)


def sidebar_item(
    icon_name: str,
    text: str,
    view_name: str,
    is_active: rx.Var[bool],
    is_theme_toggle: bool = False,
) -> rx.Component:
    return rx.el.div(
        rx.el.a(
            rx.icon(
                tag=icon_name,
                class_name=rx.cond(
                    PrintOptimizerState.theme == "dark",
                    "w-5 h-5 mr-3 text-[#A0A0A0] group-hover:text-[#F5F5F5] transition-colors",
                    "w-5 h-5 mr-3 text-[#505050] group-hover:text-black transition-colors",
                ),
            ),
            rx.el.span(
                text,
                class_name=rx.cond(
                    PrintOptimizerState.sidebar_collapsed,
                    "hidden",
                    rx.cond(
                        PrintOptimizerState.theme == "dark",
                        "text-sm font-medium text-[#A0A0A0] group-hover:text-[#F5F5F5] transition-colors",
                        "text-sm font-medium text-[#505050] group-hover:text-black transition-colors",
                    ),
                ),
            ),
            href="#",
            on_click=rx.cond(
                ~is_theme_toggle,
                PrintOptimizerState.set_active_view(
                    view_name
                ),
                PrintOptimizerState.toggle_theme,
            ),
            class_name=rx.cond(
                is_active,
                rx.cond(
                    PrintOptimizerState.theme == "dark",
                    "flex items-center p-3 rounded-lg bg-[#E63946] text-[#F5F5F5] hover:bg-opacity-80 transition-colors group",
                    "flex items-center p-3 rounded-lg bg-[#E63946] text-white hover:bg-opacity-80 transition-colors group",
                ),
                rx.cond(
                    PrintOptimizerState.theme == "dark",
                    "flex items-center p-3 rounded-lg hover:bg-[#2a2a2a] transition-colors group",
                    "flex items-center p-3 rounded-lg hover:bg-gray-200 transition-colors group",
                ),
            ),
        ),
        class_name="mb-1",
    )


def sidebar_header() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.img(
                src="/favicon.ico", class_name="h-8 w-auto"
            ),
            rx.el.span(
                "PrintOptimizer",
                class_name=rx.cond(
                    PrintOptimizerState.sidebar_collapsed,
                    "hidden",
                    rx.cond(
                        PrintOptimizerState.theme == "dark",
                        "ml-3 text-xl font-bold text-[#F5F5F5]",
                        "ml-3 text-xl font-bold text-black",
                    ),
                ),
            ),
            class_name="flex items-center",
        ),
        rx.el.button(
            rx.icon(
                tag=rx.cond(
                    PrintOptimizerState.sidebar_collapsed,
                    "align-justify",
                    "align-left",
                ),
                class_name=rx.cond(
                    PrintOptimizerState.theme == "dark",
                    "w-6 h-6 text-[#A0A0A0] hover:text-[#F5F5F5]",
                    "w-6 h-6 text-[#505050] hover:text-black",
                ),
            ),
            on_click=PrintOptimizerState.toggle_sidebar,
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "p-1 rounded hover:bg-[#2a2a2a] transition-colors",
                "p-1 rounded hover:bg-gray-200 transition-colors",
            ),
        ),
        class_name=rx.cond(
            PrintOptimizerState.theme == "dark",
            "flex items-center justify-between p-4 border-b border-[#2a2a2a]",
            "flex items-center justify-between p-4 border-b border-gray-200",
        ),
    )


def sidebar() -> rx.Component:
    nav_items = [
        ("layout-dashboard", "Summary", "summary"),
        ("shopping-cart", "Marketplaces", "marketplaces"),
        ("line-chart", "Trends", "trends"),
        ("settings-2", "Metadata", "metadata"),
        ("dollar-sign", "Costs", "costs"),
        ("upload-cloud", "Uploads", "uploads"),
        ("folder-kanban", "Projects", "projects"),
        ("clipboard-list", "Inventory", "inventory"),
        ("truck", "Material Orders", "ordering"),
        ("file-text", "Quotes", "quotations"),
        ("calendar-days", "Calendar", "calendar"),
        ("file-down", "PDF Export", "pdf_export"),
    ]
    return rx.el.aside(
        sidebar_header(),
        rx.el.nav(
            rx.foreach(
                nav_items,
                lambda item: sidebar_item(
                    item[0],
                    item[1],
                    item[2],
                    PrintOptimizerState.active_view
                    == item[2],
                ),
            ),
            class_name="flex-grow p-4 space-y-1 overflow-y-auto",
        ),
        rx.el.div(
            sidebar_item(
                icon_name=rx.cond(
                    PrintOptimizerState.theme == "dark",
                    "moon",
                    "sun",
                ),
                text=rx.cond(
                    PrintOptimizerState.theme == "dark",
                    "Dark Mode",
                    "Light Mode",
                ),
                view_name="toggle_theme",
                is_active=rx.Var.create(False),
                is_theme_toggle=True,
            ),
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "p-4 border-t border-[#2a2a2a]",
                "p-4 border-t border-gray-200",
            ),
        ),
        class_name=rx.cond(
            PrintOptimizerState.sidebar_collapsed,
            rx.cond(
                PrintOptimizerState.theme == "dark",
                "w-20 bg-[#1E1E1E] text-[#F5F5F5] flex flex-col transition-all duration-300 ease-in-out",
                "w-20 bg-white text-black flex flex-col transition-all duration-300 ease-in-out",
            ),
            rx.cond(
                PrintOptimizerState.theme == "dark",
                "w-64 bg-[#1E1E1E] text-[#F5F5F5] flex flex-col transition-all duration-300 ease-in-out",
                "w-64 bg-white text-black flex flex-col transition-all duration-300 ease-in-out",
            ),
        ),
        style={"height": "100vh"},
    )