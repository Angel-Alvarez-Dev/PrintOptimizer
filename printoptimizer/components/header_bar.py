import reflex as rx
from printoptimizer.states.print_optimizer_state import (
    PrintOptimizerState,
)


def header_bar() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.h1(
                PrintOptimizerState.current_page_title,
                class_name=rx.cond(
                    PrintOptimizerState.theme == "dark",
                    "text-2xl font-semibold text-[#F5F5F5]",
                    "text-2xl font-semibold text-black",
                ),
            ),
            rx.el.div(
                rx.icon(
                    tag="bell",
                    class_name=rx.cond(
                        PrintOptimizerState.theme == "dark",
                        "w-6 h-6 text-[#A0A0A0] hover:text-[#F5F5F5] cursor-pointer",
                        "w-6 h-6 text-[#505050] hover:text-black cursor-pointer",
                    ),
                ),
                rx.el.button(
                    rx.icon(
                        tag="mail",
                        class_name=rx.cond(
                            PrintOptimizerState.theme
                            == "dark",
                            "w-6 h-6 text-[#A0A0A0] group-hover:text-[#F5F5F5]",
                            "w-6 h-6 text-[#505050] group-hover:text-black",
                        ),
                    ),
                    on_click=lambda: PrintOptimizerState.set_active_view(
                        "mail_inbox"
                    ),
                    class_name=rx.cond(
                        PrintOptimizerState.theme == "dark",
                        "p-1 rounded hover:bg-[#2a2a2a] transition-colors ml-4 group",
                        "p-1 rounded hover:bg-gray-200 transition-colors ml-4 group",
                    ),
                ),
                rx.el.img(
                    src="/favicon.ico",
                    class_name="w-8 h-8 rounded-full ml-4 cursor-pointer",
                ),
                class_name="flex items-center",
            ),
            class_name="flex items-center justify-between w-full",
        ),
        class_name=rx.cond(
            PrintOptimizerState.theme == "dark",
            "bg-[#1E1E1E] p-4 sticky top-0 z-10 border-b border-[#2a2a2a]",
            "bg-white p-4 sticky top-0 z-10 border-b border-gray-200",
        ),
    )