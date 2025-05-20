import reflex as rx
from printoptimizer.states.print_optimizer_state import (
    PrintOptimizerState,
    CalendarEventType,
)
from typing import get_args


def add_event_form() -> rx.Component:
    return rx.el.form(
        rx.el.h3(
            "Add New Calendar Event",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "text-lg font-semibold text-[#F5F5F5] mb-3",
                "text-lg font-semibold text-black mb-3",
            ),
        ),
        rx.el.label(
            "Title:",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "block text-sm font-medium text-[#A0A0A0] mb-1",
                "block text-sm font-medium text-gray-700 mb-1",
            ),
        ),
        rx.el.input(
            name="title",
            placeholder="Event title",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "w-full p-2 mb-3 bg-[#2a2a2a] text-[#F5F5F5] border border-[#333333] rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
                "w-full p-2 mb-3 bg-white text-black border border-gray-300 rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
            ),
        ),
        rx.el.label(
            "Start Date:",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "block text-sm font-medium text-[#A0A0A0] mb-1",
                "block text-sm font-medium text-gray-700 mb-1",
            ),
        ),
        rx.el.input(
            name="start_date",
            type="date",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "w-full p-2 mb-3 bg-[#2a2a2a] text-[#F5F5F5] border border-[#333333] rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
                "w-full p-2 mb-3 bg-white text-black border border-gray-300 rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
            ),
        ),
        rx.el.label(
            "End Date (Optional):",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "block text-sm font-medium text-[#A0A0A0] mb-1",
                "block text-sm font-medium text-gray-700 mb-1",
            ),
        ),
        rx.el.input(
            name="end_date",
            type="date",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "w-full p-2 mb-3 bg-[#2a2a2a] text-[#F5F5F5] border border-[#333333] rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
                "w-full p-2 mb-3 bg-white text-black border border-gray-300 rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
            ),
        ),
        rx.el.label(
            "Event Type:",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "block text-sm font-medium text-[#A0A0A0] mb-1",
                "block text-sm font-medium text-gray-700 mb-1",
            ),
        ),
        rx.el.select(
            rx.foreach(
                list(get_args(CalendarEventType)),
                lambda opt: rx.el.option(opt, value=opt),
            ),
            name="event_type",
            default_value="General",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "w-full p-2 mb-3 bg-[#2a2a2a] text-[#F5F5F5] border border-[#333333] rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
                "w-full p-2 mb-3 bg-white text-black border border-gray-300 rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
            ),
        ),
        rx.el.label(
            "Color (Hex):",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "block text-sm font-medium text-[#A0A0A0] mb-1",
                "block text-sm font-medium text-gray-700 mb-1",
            ),
        ),
        rx.el.input(
            name="color",
            placeholder="#3182CE",
            default_value="#3182CE",
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
                on_click=PrintOptimizerState.toggle_add_calendar_event_form,
                class_name=rx.cond(
                    PrintOptimizerState.theme == "dark",
                    "p-2 bg-gray-600 text-[#F5F5F5] rounded-md hover:bg-gray-500 transition-colors",
                    "p-2 bg-gray-300 text-black rounded-md hover:bg-gray-400 transition-colors",
                ),
            ),
            rx.el.button(
                "Add Event",
                type="submit",
                class_name="p-2 bg-[#E63946] text-[#F5F5F5] rounded-md hover:bg-opacity-80 transition-colors",
            ),
            class_name="flex justify-end space-x-2 mt-2",
        ),
        on_submit=PrintOptimizerState.add_calendar_event_manually,
        reset_on_submit=True,
        class_name=rx.cond(
            PrintOptimizerState.theme == "dark",
            "p-4 bg-[#252525] rounded-lg shadow-md mb-6",
            "p-4 bg-white rounded-lg shadow-md mb-6 border border-gray-200",
        ),
    )


def interactive_calendar() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2(
                "Interactive Calendar",
                class_name=rx.cond(
                    PrintOptimizerState.theme == "dark",
                    "text-xl font-semibold text-[#F5F5F5]",
                    "text-xl font-semibold text-black",
                ),
            ),
            rx.el.button(
                rx.cond(
                    PrintOptimizerState.show_add_calendar_event_form,
                    "Close Form",
                    "Add Event Manually",
                ),
                on_click=PrintOptimizerState.toggle_add_calendar_event_form,
                class_name="p-2 bg-[#E63946] text-[#F5F5F5] rounded-md hover:bg-opacity-80 transition-colors",
            ),
            class_name="flex justify-between items-center mb-4",
        ),
        rx.cond(
            PrintOptimizerState.show_add_calendar_event_form,
            add_event_form(),
        ),
        rx.el.div(
            rx.foreach(
                PrintOptimizerState.calendar_events_data,
                lambda event: rx.el.div(
                    rx.el.div(
                        rx.el.p(
                            f"ID: {event['id']} - {event['title']} ({event['type']})",
                            class_name=rx.cond(
                                PrintOptimizerState.theme
                                == "dark",
                                "text-sm text-[#F5F5F5] font-medium",
                                "text-sm text-black font-medium",
                            ),
                        ),
                        rx.el.button(
                            rx.icon(
                                tag="trash-2",
                                class_name="w-4 h-4",
                            ),
                            on_click=lambda: PrintOptimizerState.remove_calendar_event_by_id(
                                event["id"]
                            ),
                            class_name="p-1 text-red-500 hover:text-red-400",
                        ),
                        class_name="flex justify-between items-center",
                    ),
                    rx.el.p(
                        f"""Date: {event['start']}{rx.cond(event['end'] != event['start'], f" to {event['end']}", '')}""",
                        class_name=rx.cond(
                            PrintOptimizerState.theme
                            == "dark",
                            "text-xs text-[#A0A0A0]",
                            "text-xs text-gray-600",
                        ),
                    ),
                    style={
                        "borderLeft": f"4px solid {event['color']}"
                    },
                    class_name=rx.cond(
                        PrintOptimizerState.theme == "dark",
                        "p-2 mb-2 bg-[#2a2a2a] rounded-r-md",
                        "p-2 mb-2 bg-white rounded-r-md border border-gray-200",
                    ),
                ),
            ),
            class_name="max-h-96 overflow-y-auto",
        ),
        rx.cond(
            PrintOptimizerState.calendar_events_data.length()
            == 0,
            rx.el.p(
                "No events scheduled.",
                class_name=rx.cond(
                    PrintOptimizerState.theme == "dark",
                    "text-center text-[#A0A0A0] py-4",
                    "text-center text-gray-500 py-4",
                ),
            ),
        ),
        rx.el.p(
            "A full interactive calendar with drag-and-drop would be implemented here.",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "text-[#A0A0A0] mt-4 text-sm",
                "text-gray-600 mt-4 text-sm",
            ),
        ),
        class_name=rx.cond(
            PrintOptimizerState.theme == "dark",
            "mt-8 p-4 bg-[#252525] rounded-lg shadow-md",
            "mt-8 p-4 bg-white rounded-lg shadow-md border border-gray-200",
        ),
    )