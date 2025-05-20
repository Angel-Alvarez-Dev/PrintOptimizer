import reflex as rx
from printoptimizer.states.print_optimizer_state import (
    PrintOptimizerState,
)


def ai_metadata_widget() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "AI Metadata Generator",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "text-xl font-semibold text-[#F5F5F5] mb-4",
                "text-xl font-semibold text-black mb-4",
            ),
        ),
        rx.el.div(
            rx.el.form(
                rx.el.label(
                    "Target Platform:",
                    class_name=rx.cond(
                        PrintOptimizerState.theme == "dark",
                        "block text-sm font-medium text-[#A0A0A0] mb-1",
                        "block text-sm font-medium text-gray-700 mb-1",
                    ),
                ),
                rx.el.select(
                    rx.foreach(
                        [
                            "Thingiverse",
                            "MyMiniFactory",
                            "Cults3D",
                            "Patreon",
                            "General SEO",
                        ],
                        lambda opt: rx.el.option(
                            opt, value=opt
                        ),
                    ),
                    name="platform",
                    class_name=rx.cond(
                        PrintOptimizerState.theme == "dark",
                        "w-full p-2 mb-4 bg-[#2a2a2a] text-[#F5F5F5] border border-[#333333] rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
                        "w-full p-2 mb-4 bg-white text-black border border-gray-300 rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
                    ),
                ),
                rx.el.label(
                    "Generated Title:",
                    class_name=rx.cond(
                        PrintOptimizerState.theme == "dark",
                        "block text-sm font-medium text-[#A0A0A0] mb-1",
                        "block text-sm font-medium text-gray-700 mb-1",
                    ),
                ),
                rx.el.input(
                    default_value=PrintOptimizerState.ai_metadata[
                        "title"
                    ],
                    is_read_only=True,
                    class_name=rx.cond(
                        PrintOptimizerState.theme == "dark",
                        "w-full p-2 mb-4 bg-[#2a2a2a] text-[#F5F5F5] border border-[#333333] rounded-md",
                        "w-full p-2 mb-4 bg-gray-100 text-black border border-gray-300 rounded-md",
                    ),
                ),
                rx.el.label(
                    "Generated Description:",
                    class_name=rx.cond(
                        PrintOptimizerState.theme == "dark",
                        "block text-sm font-medium text-[#A0A0A0] mb-1",
                        "block text-sm font-medium text-gray-700 mb-1",
                    ),
                ),
                rx.el.textarea(
                    default_value=PrintOptimizerState.ai_metadata[
                        "description"
                    ],
                    is_read_only=True,
                    rows=4,
                    class_name=rx.cond(
                        PrintOptimizerState.theme == "dark",
                        "w-full p-2 mb-4 bg-[#2a2a2a] text-[#F5F5F5] border border-[#333333] rounded-md",
                        "w-full p-2 mb-4 bg-gray-100 text-black border border-gray-300 rounded-md",
                    ),
                ),
                rx.el.label(
                    "Generated Tags:",
                    class_name=rx.cond(
                        PrintOptimizerState.theme == "dark",
                        "block text-sm font-medium text-[#A0A0A0] mb-1",
                        "block text-sm font-medium text-gray-700 mb-1",
                    ),
                ),
                rx.el.input(
                    default_value=PrintOptimizerState.ai_metadata[
                        "tags"
                    ].join(
                        ", "
                    ),
                    is_read_only=True,
                    class_name=rx.cond(
                        PrintOptimizerState.theme == "dark",
                        "w-full p-2 mb-4 bg-[#2a2a2a] text-[#F5F5F5] border border-[#333333] rounded-md",
                        "w-full p-2 mb-4 bg-gray-100 text-black border border-gray-300 rounded-md",
                    ),
                ),
                rx.el.button(
                    "Generate Metadata",
                    on_click=PrintOptimizerState.generate_metadata,
                    type="button",
                    class_name="w-full p-2 bg-[#E63946] text-[#F5F5F5] rounded-md hover:bg-opacity-80 transition-colors",
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