import reflex as rx
from printoptimizer.states.print_optimizer_state import (
    PrintOptimizerState,
    MailMessage,
)


def mail_item_card(mail: MailMessage) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h4(
                mail["subject"],
                class_name=rx.cond(
                    PrintOptimizerState.theme == "dark",
                    "text-md font-semibold text-[#F5F5F5]",
                    "text-md font-semibold text-black",
                ),
            ),
            rx.el.p(
                f"From: {mail['sender']} | Received: {mail['received_at']}",
                class_name=rx.cond(
                    PrintOptimizerState.theme == "dark",
                    "text-xs text-[#A0A0A0]",
                    "text-xs text-gray-600",
                ),
            ),
            class_name="flex-1",
        ),
        rx.el.p(
            mail["body"],
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "text-sm text-[#F5F5F5] my-2",
                "text-sm text-black my-2",
            ),
        ),
        rx.cond(
            mail["processed"],
            rx.el.div(
                rx.icon(
                    tag="check_check",
                    class_name="w-4 h-4 mr-1 text-green-500",
                ),
                rx.el.span(
                    "Processed",
                    class_name="text-xs text-green-500",
                ),
                class_name="flex items-center",
            ),
            rx.el.button(
                "Process Mail",
                on_click=lambda: PrintOptimizerState.process_mail(
                    mail["id"]
                ),
                class_name="mt-1 text-xs bg-[#E63946] text-[#F5F5F5] px-3 py-1 rounded hover:bg-opacity-80 transition-colors",
            ),
        ),
        class_name=rx.cond(
            PrintOptimizerState.theme == "dark",
            "p-4 bg-[#2a2a2a] rounded-md shadow mb-3",
            "p-4 bg-white rounded-md shadow mb-3 border border-gray-200",
        ),
    )


def mail_inbox() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2(
                "Mail Inbox",
                class_name=rx.cond(
                    PrintOptimizerState.theme == "dark",
                    "text-xl font-semibold text-[#F5F5F5]",
                    "text-xl font-semibold text-black",
                ),
            ),
            rx.el.button(
                "Receive Sample Mail",
                on_click=PrintOptimizerState.add_sample_mail,
                class_name="p-2 bg-[#E63946] text-[#F5F5F5] rounded-md hover:bg-opacity-80 transition-colors",
            ),
            class_name="flex justify-between items-center mb-6",
        ),
        rx.cond(
            PrintOptimizerState.mail_inbox_data.length()
            == 0,
            rx.el.p(
                "Your inbox is empty.",
                class_name=rx.cond(
                    PrintOptimizerState.theme == "dark",
                    "text-center text-[#A0A0A0] py-10",
                    "text-center text-gray-500 py-10",
                ),
            ),
            rx.el.div(
                rx.foreach(
                    PrintOptimizerState.mail_inbox_data,
                    mail_item_card,
                ),
                class_name="max-h-[70vh] overflow-y-auto",
            ),
        ),
        class_name=rx.cond(
            PrintOptimizerState.theme == "dark",
            "mt-8 p-4 bg-[#252525] rounded-lg shadow-md",
            "mt-8 p-4 bg-white rounded-lg shadow-md border border-gray-200",
        ),
    )