import reflex as rx
from printoptimizer.states.print_optimizer_state import (
    PrintOptimizerState,
    QuoteItem,
    Quote,
)


def current_quote_item_row(
    item: QuoteItem, index: int
) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            item["description"],
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "py-2 px-4 text-[#F5F5F5]",
                "py-2 px-4 text-black",
            ),
        ),
        rx.el.td(
            rx.el.input(
                default_value=item["quantity"].to_string(),
                on_change=lambda val: PrintOptimizerState.update_current_quote_item_quantity(
                    item["id"], val
                ),
                type="number",
                min="1",
                class_name=rx.cond(
                    PrintOptimizerState.theme == "dark",
                    "w-20 p-1 bg-[#2a2a2a] text-[#F5F5F5] border border-[#333333] rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
                    "w-20 p-1 bg-white text-black border border-gray-300 rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
                ),
            ),
            class_name="py-2 px-4",
        ),
        rx.el.td(
            f"${item['unit_price']:.2f}",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "py-2 px-4 text-[#F5F5F5]",
                "py-2 px-4 text-black",
            ),
        ),
        rx.el.td(
            f"${item['quantity'] * item['unit_price']:.2f}",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "py-2 px-4 text-[#F5F5F5] text-right",
                "py-2 px-4 text-black text-right",
            ),
        ),
        rx.el.td(
            rx.el.button(
                rx.icon(
                    tag="trash-2", class_name="w-4 h-4"
                ),
                on_click=lambda: PrintOptimizerState.remove_item_from_current_quote(
                    item["id"]
                ),
                class_name="p-1 text-red-500 hover:text-red-400",
            ),
            class_name="py-2 px-4 text-center",
        ),
    )


def saved_quote_card(quote: Quote) -> rx.Component:
    return rx.el.div(
        rx.el.h4(
            f"Quote #{quote['id']} - {quote['client_name']}",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "text-md font-semibold text-[#F5F5F5]",
                "text-md font-semibold text-black",
            ),
        ),
        rx.el.p(
            f"Date: {quote['date_created']}",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "text-xs text-[#A0A0A0]",
                "text-xs text-gray-600",
            ),
        ),
        rx.el.p(
            f"Items: {quote['items'].length()}",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "text-xs text-[#A0A0A0]",
                "text-xs text-gray-600",
            ),
        ),
        class_name=rx.cond(
            PrintOptimizerState.theme == "dark",
            "p-3 bg-[#2a2a2a] rounded-md shadow",
            "p-3 bg-white rounded-md shadow border border-gray-200",
        ),
    )


def quotation_area() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "Quotation Area",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "text-xl font-semibold text-[#F5F5F5] mb-4",
                "text-xl font-semibold text-black mb-4",
            ),
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    "Build New Quote",
                    class_name=rx.cond(
                        PrintOptimizerState.theme == "dark",
                        "text-lg font-semibold text-[#F5F5F5] mb-3",
                        "text-lg font-semibold text-black mb-3",
                    ),
                ),
                rx.el.label(
                    "Client Name:",
                    class_name=rx.cond(
                        PrintOptimizerState.theme == "dark",
                        "block text-sm font-medium text-[#A0A0A0] mb-1",
                        "block text-sm font-medium text-gray-700 mb-1",
                    ),
                ),
                rx.el.input(
                    default_value=PrintOptimizerState.current_quote_client_name,
                    placeholder="Enter client name",
                    on_change=PrintOptimizerState.set_current_quote_client_name,
                    class_name=rx.cond(
                        PrintOptimizerState.theme == "dark",
                        "w-full p-2 mb-3 bg-[#2a2a2a] text-[#F5F5F5] border border-[#333333] rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
                        "w-full p-2 mb-3 bg-white text-black border border-gray-300 rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
                    ),
                ),
                rx.el.h4(
                    "Add Item:",
                    class_name=rx.cond(
                        PrintOptimizerState.theme == "dark",
                        "text-md font-semibold text-[#A0A0A0] mt-4 mb-2",
                        "text-md font-semibold text-gray-700 mt-4 mb-2",
                    ),
                ),
                rx.el.div(
                    rx.el.input(
                        default_value=PrintOptimizerState.new_quote_item_description,
                        placeholder="Item Description",
                        on_change=PrintOptimizerState.set_new_quote_item_description,
                        class_name=rx.cond(
                            PrintOptimizerState.theme
                            == "dark",
                            "p-2 bg-[#2a2a2a] text-[#F5F5F5] border border-[#333333] rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
                            "p-2 bg-white text-black border border-gray-300 rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
                        ),
                    ),
                    rx.el.input(
                        default_value=PrintOptimizerState.new_quote_item_quantity.to_string(),
                        type="number",
                        min="1",
                        placeholder="Quantity",
                        on_change=PrintOptimizerState.set_new_quote_item_quantity,
                        class_name=rx.cond(
                            PrintOptimizerState.theme
                            == "dark",
                            "p-2 bg-[#2a2a2a] text-[#F5F5F5] border border-[#333333] rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
                            "p-2 bg-white text-black border border-gray-300 rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
                        ),
                    ),
                    rx.el.input(
                        default_value=PrintOptimizerState.new_quote_item_unit_price.to_string(),
                        type="number",
                        min="0",
                        step="0.01",
                        placeholder="Unit Price ($)",
                        on_change=PrintOptimizerState.set_new_quote_item_unit_price,
                        class_name=rx.cond(
                            PrintOptimizerState.theme
                            == "dark",
                            "p-2 bg-[#2a2a2a] text-[#F5F5F5] border border-[#333333] rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
                            "p-2 bg-white text-black border border-gray-300 rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
                        ),
                    ),
                    rx.el.button(
                        "Add Item",
                        on_click=PrintOptimizerState.add_item_to_current_quote,
                        class_name="p-2 bg-[#E63946] text-[#F5F5F5] rounded-md hover:bg-opacity-80 transition-colors h-full",
                    ),
                    class_name="grid grid-cols-[2fr_1fr_1fr_auto] gap-2 mb-4 items-end",
                ),
                rx.el.h4(
                    "Current Quote Items:",
                    class_name=rx.cond(
                        PrintOptimizerState.theme == "dark",
                        "text-md font-semibold text-[#A0A0A0] mt-4 mb-2",
                        "text-md font-semibold text-gray-700 mt-4 mb-2",
                    ),
                ),
                rx.cond(
                    PrintOptimizerState.current_quote_items.length()
                    == 0,
                    rx.el.p(
                        "No items added to the current quote.",
                        class_name=rx.cond(
                            PrintOptimizerState.theme
                            == "dark",
                            "text-[#A0A0A0] text-center py-3",
                            "text-gray-500 text-center py-3",
                        ),
                    ),
                    rx.el.table(
                        rx.el.thead(
                            rx.el.tr(
                                rx.el.th(
                                    "Description",
                                    class_name=rx.cond(
                                        PrintOptimizerState.theme
                                        == "dark",
                                        "py-2 px-4 text-left text-sm font-medium text-[#A0A0A0] uppercase",
                                        "py-2 px-4 text-left text-sm font-medium text-gray-500 uppercase",
                                    ),
                                ),
                                rx.el.th(
                                    "Quantity",
                                    class_name=rx.cond(
                                        PrintOptimizerState.theme
                                        == "dark",
                                        "py-2 px-4 text-left text-sm font-medium text-[#A0A0A0] uppercase",
                                        "py-2 px-4 text-left text-sm font-medium text-gray-500 uppercase",
                                    ),
                                ),
                                rx.el.th(
                                    "Unit Price",
                                    class_name=rx.cond(
                                        PrintOptimizerState.theme
                                        == "dark",
                                        "py-2 px-4 text-left text-sm font-medium text-[#A0A0A0] uppercase",
                                        "py-2 px-4 text-left text-sm font-medium text-gray-500 uppercase",
                                    ),
                                ),
                                rx.el.th(
                                    "Total",
                                    class_name=rx.cond(
                                        PrintOptimizerState.theme
                                        == "dark",
                                        "py-2 px-4 text-right text-sm font-medium text-[#A0A0A0] uppercase",
                                        "py-2 px-4 text-right text-sm font-medium text-gray-500 uppercase",
                                    ),
                                ),
                                rx.el.th(
                                    "Actions",
                                    class_name=rx.cond(
                                        PrintOptimizerState.theme
                                        == "dark",
                                        "py-2 px-4 text-center text-sm font-medium text-[#A0A0A0] uppercase",
                                        "py-2 px-4 text-center text-sm font-medium text-gray-500 uppercase",
                                    ),
                                ),
                            )
                        ),
                        rx.el.tbody(
                            rx.foreach(
                                PrintOptimizerState.current_quote_items,
                                lambda item, index: current_quote_item_row(
                                    item, index
                                ),
                            )
                        ),
                        class_name="w-full mb-4",
                    ),
                ),
                rx.el.label(
                    "Markup (%):",
                    class_name=rx.cond(
                        PrintOptimizerState.theme == "dark",
                        "block text-sm font-medium text-[#A0A0A0] mb-1 mt-4",
                        "block text-sm font-medium text-gray-700 mb-1 mt-4",
                    ),
                ),
                rx.el.input(
                    default_value=PrintOptimizerState.current_quote_markup_percentage.to_string(),
                    type="number",
                    min="0",
                    step="0.01",
                    on_change=PrintOptimizerState.set_current_quote_markup_percentage,
                    class_name=rx.cond(
                        PrintOptimizerState.theme == "dark",
                        "w-full p-2 mb-3 bg-[#2a2a2a] text-[#F5F5F5] border border-[#333333] rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
                        "w-full p-2 mb-3 bg-white text-black border border-gray-300 rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
                    ),
                ),
                rx.el.div(
                    rx.el.p(
                        f"Subtotal: ${PrintOptimizerState.current_quote_subtotal:.2f}",
                        class_name=rx.cond(
                            PrintOptimizerState.theme
                            == "dark",
                            "text-[#F5F5F5]",
                            "text-black",
                        ),
                    ),
                    rx.el.p(
                        f"Markup Amount: ${PrintOptimizerState.current_quote_markup_amount:.2f}",
                        class_name=rx.cond(
                            PrintOptimizerState.theme
                            == "dark",
                            "text-[#F5F5F5]",
                            "text-black",
                        ),
                    ),
                    rx.el.p(
                        f"Total: ${PrintOptimizerState.current_quote_total:.2f}",
                        class_name="text-lg font-bold text-[#E63946]",
                    ),
                    class_name="text-right mt-4 mb-4",
                ),
                rx.el.div(
                    rx.link(
                        rx.el.button(
                            rx.icon(
                                tag="message-circle",
                                class_name="mr-2",
                            ),
                            "Send via WhatsApp",
                            class_name="flex items-center p-2 bg-green-500 text-white rounded-md hover:bg-green-600 transition-colors disabled:opacity-50",
                            disabled=PrintOptimizerState.current_quote_items.length()
                            == 0,
                        ),
                        href=PrintOptimizerState.whatsapp_link,
                        is_external=True,
                    ),
                    rx.link(
                        rx.el.button(
                            rx.icon(
                                tag="mail",
                                class_name="mr-2",
                            ),
                            "Send via Gmail",
                            class_name="flex items-center p-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 transition-colors disabled:opacity-50",
                            disabled=PrintOptimizerState.current_quote_items.length()
                            == 0,
                        ),
                        href=PrintOptimizerState.gmail_link,
                        is_external=True,
                    ),
                    rx.el.button(
                        "Save Quote",
                        on_click=PrintOptimizerState.save_current_quote,
                        class_name="p-2 bg-[#E63946] text-[#F5F5F5] rounded-md hover:bg-opacity-80 transition-colors disabled:opacity-50",
                        disabled=PrintOptimizerState.current_quote_items.length()
                        == 0,
                    ),
                    rx.el.button(
                        "Clear Quote",
                        on_click=PrintOptimizerState.clear_current_quote,
                        class_name=rx.cond(
                            PrintOptimizerState.theme
                            == "dark",
                            "p-2 bg-gray-600 text-[#F5F5F5] rounded-md hover:bg-gray-500 transition-colors",
                            "p-2 bg-gray-300 text-black rounded-md hover:bg-gray-400 transition-colors",
                        ),
                    ),
                    class_name="flex justify-end space-x-2 mt-4",
                ),
                class_name=rx.cond(
                    PrintOptimizerState.theme == "dark",
                    "flex-1 p-4 bg-[#252525] rounded-lg shadow-md",
                    "flex-1 p-4 bg-white rounded-lg shadow-md border border-gray-200",
                ),
            ),
            rx.el.div(
                rx.el.h3(
                    "Saved Quotes",
                    class_name=rx.cond(
                        PrintOptimizerState.theme == "dark",
                        "text-lg font-semibold text-[#F5F5F5] mb-3",
                        "text-lg font-semibold text-black mb-3",
                    ),
                ),
                rx.cond(
                    PrintOptimizerState.quotes_data.length()
                    == 0,
                    rx.el.p(
                        "No quotes saved yet.",
                        class_name=rx.cond(
                            PrintOptimizerState.theme
                            == "dark",
                            "text-[#A0A0A0] text-center py-4",
                            "text-gray-500 text-center py-4",
                        ),
                    ),
                    rx.el.div(
                        rx.foreach(
                            PrintOptimizerState.quotes_data,
                            saved_quote_card,
                        ),
                        class_name="space-y-3 max-h-[60vh] overflow-y-auto p-1",
                    ),
                ),
                class_name=rx.cond(
                    PrintOptimizerState.theme == "dark",
                    "flex-1 p-4 bg-[#1E1E1E] rounded-lg shadow-inner ml-6 w-[300px]",
                    "flex-1 p-4 bg-gray-50 rounded-lg shadow-inner ml-6 w-[300px] border border-gray-200",
                ),
            ),
            class_name="flex flex-row mt-8",
        ),
    )