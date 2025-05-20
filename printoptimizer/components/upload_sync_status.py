import reflex as rx
from printoptimizer.states.print_optimizer_state import (
    PrintOptimizerState,
    UploadItem,
)


def status_indicator(status: rx.Var[str]) -> rx.Component:
    return rx.match(
        status,
        (
            "Synced",
            rx.el.div(
                rx.icon(
                    tag="check_check",
                    class_name="text-green-500 w-4 h-4 mr-1",
                ),
                rx.el.span(
                    "Synced",
                    class_name="text-green-500 text-xs",
                ),
                class_name="flex items-center",
            ),
        ),
        (
            "Uploading",
            rx.el.div(
                rx.icon(
                    tag="cloud_upload",
                    class_name="text-blue-500 w-4 h-4 mr-1 animate-pulse",
                ),
                rx.el.span(
                    "Uploading",
                    class_name="text-blue-500 text-xs",
                ),
                class_name="flex items-center",
            ),
        ),
        (
            "Processing",
            rx.el.div(
                rx.icon(
                    tag="loader",
                    class_name="text-yellow-500 w-4 h-4 mr-1 animate-spin",
                ),
                rx.el.span(
                    "Processing",
                    class_name="text-yellow-500 text-xs",
                ),
                class_name="flex items-center",
            ),
        ),
        (
            "Pending",
            rx.el.div(
                rx.icon(
                    tag="clock",
                    class_name="text-gray-500 w-4 h-4 mr-1",
                ),
                rx.el.span(
                    "Pending",
                    class_name="text-gray-500 text-xs",
                ),
                class_name="flex items-center",
            ),
        ),
        (
            "Error",
            rx.el.div(
                rx.icon(
                    tag="flag_triangle_right",
                    class_name="text-red-500 w-4 h-4 mr-1",
                ),
                rx.el.span(
                    "Error",
                    class_name="text-red-500 text-xs",
                ),
                class_name="flex items-center",
            ),
        ),
        rx.el.span(
            status,
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "text-xs text-[#A0A0A0]",
                "text-xs text-gray-600",
            ),
        ),
    )


def upload_item_card(item: UploadItem) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.p(
                item["name"],
                class_name=rx.cond(
                    PrintOptimizerState.theme == "dark",
                    "text-sm font-medium text-[#F5F5F5]",
                    "text-sm font-medium text-black",
                ),
            ),
            rx.el.p(
                item["type"],
                class_name=rx.cond(
                    PrintOptimizerState.theme == "dark",
                    "text-xs text-[#A0A0A0]",
                    "text-xs text-gray-600",
                ),
            ),
            class_name="flex-1",
        ),
        rx.el.div(
            rx.el.div(
                style={
                    "width": item["progress"].to_string()
                    + "%"
                },
                class_name="h-2 rounded-full bg-[#E63946]",
            ),
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "w-full bg-[#333333] rounded-full h-2 my-1",
                "w-full bg-gray-300 rounded-full h-2 my-1",
            ),
        ),
        status_indicator(item["status"]),
        rx.cond(
            item["status"] == "Error",
            rx.el.button(
                "Retry",
                on_click=lambda: PrintOptimizerState.retry_upload(
                    item["name"]
                ),
                class_name="mt-1 text-xs bg-[#E63946] text-[#F5F5F5] px-2 py-0.5 rounded hover:bg-opacity-80",
            ),
        ),
        class_name=rx.cond(
            PrintOptimizerState.theme == "dark",
            "p-3 bg-[#2a2a2a] rounded-md shadow flex flex-col space-y-1",
            "p-3 bg-white rounded-md shadow flex flex-col space-y-1 border border-gray-200",
        ),
    )


def upload_sync_status() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "Upload & Sync Status",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "text-xl font-semibold text-[#F5F5F5] mb-4",
                "text-xl font-semibold text-black mb-4",
            ),
        ),
        rx.el.div(
            rx.upload(
                rx.el.div(
                    rx.icon(
                        tag="cloud_upload",
                        class_name=rx.cond(
                            PrintOptimizerState.theme
                            == "dark",
                            "w-8 h-8 mb-2 text-[#A0A0A0]",
                            "w-8 h-8 mb-2 text-gray-500",
                        ),
                    ),
                    rx.el.p(
                        "Drag & drop STL/3MF files or click to upload",
                        class_name=rx.cond(
                            PrintOptimizerState.theme
                            == "dark",
                            "text-sm text-[#A0A0A0]",
                            "text-sm text-gray-600",
                        ),
                    ),
                    class_name=rx.cond(
                        PrintOptimizerState.theme == "dark",
                        "flex flex-col items-center justify-center p-6 border-2 border-dashed border-[#333333] rounded-lg cursor-pointer hover:border-[#E63946] transition-colors",
                        "flex flex-col items-center justify-center p-6 border-2 border-dashed border-gray-300 rounded-lg cursor-pointer hover:border-[#E63946] transition-colors",
                    ),
                ),
                id="file_upload",
            ),
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "mb-4 bg-[#252525] rounded-lg p-4",
                "mb-4 bg-white rounded-lg p-4 border border-gray-200",
            ),
        ),
        rx.el.div(
            rx.foreach(
                PrintOptimizerState.uploads_data,
                upload_item_card,
            ),
            class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4",
        ),
        class_name="mt-8",
    )