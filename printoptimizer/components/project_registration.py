import reflex as rx
from printoptimizer.states.print_optimizer_state import (
    PrintOptimizerState,
    ProjectEntry,
)


def project_card(project: ProjectEntry) -> rx.Component:
    return rx.el.div(
        rx.el.h4(
            project["name"],
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "text-md font-semibold text-[#F5F5F5]",
                "text-md font-semibold text-black",
            ),
        ),
        rx.el.p(
            f"Client: {project['client']}",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "text-xs text-[#A0A0A0]",
                "text-xs text-gray-600",
            ),
        ),
        rx.el.p(
            f"Platform: {project['platform']}",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "text-xs text-[#A0A0A0]",
                "text-xs text-gray-600",
            ),
        ),
        rx.el.p(
            f"Due: {project['due_date']}",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "text-xs text-[#A0A0A0]",
                "text-xs text-gray-600",
            ),
        ),
        rx.el.p(
            f"Budget: ${project['budget']:.2f}",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "text-xs text-[#A0A0A0]",
                "text-xs text-gray-600",
            ),
        ),
        rx.el.span(
            project["status"],
            class_name="mt-2 inline-block px-2 py-0.5 text-xs rounded-full bg-[#E63946] text-[#F5F5F5]",
        ),
        class_name=rx.cond(
            PrintOptimizerState.theme == "dark",
            "p-4 bg-[#2a2a2a] rounded-md shadow",
            "p-4 bg-white rounded-md shadow border border-gray-200",
        ),
    )


def project_form() -> rx.Component:
    return rx.el.form(
        rx.el.h3(
            "Add New Project",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "text-lg font-semibold text-[#F5F5F5] mb-3",
                "text-lg font-semibold text-black mb-3",
            ),
        ),
        rx.el.label(
            "Project Name:",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "block text-sm font-medium text-[#A0A0A0] mb-1",
                "block text-sm font-medium text-gray-700 mb-1",
            ),
        ),
        rx.el.input(
            name="name",
            placeholder="Enter project name",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "w-full p-2 mb-3 bg-[#2a2a2a] text-[#F5F5F5] border border-[#333333] rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
                "w-full p-2 mb-3 bg-white text-black border border-gray-300 rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
            ),
        ),
        rx.el.label(
            "Client:",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "block text-sm font-medium text-[#A0A0A0] mb-1",
                "block text-sm font-medium text-gray-700 mb-1",
            ),
        ),
        rx.el.input(
            name="client",
            placeholder="Client name",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "w-full p-2 mb-3 bg-[#2a2a2a] text-[#F5F5F5] border border-[#333333] rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
                "w-full p-2 mb-3 bg-white text-black border border-gray-300 rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
            ),
        ),
        rx.el.label(
            "Platform:",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "block text-sm font-medium text-[#A0A0A0] mb-1",
                "block text-sm font-medium text-gray-700 mb-1",
            ),
        ),
        rx.el.select(
            rx.foreach(
                [
                    "Direct",
                    "Thingiverse",
                    "MyMiniFactory",
                    "Cults3D",
                    "Patreon",
                ],
                lambda p: rx.el.option(p, value=p),
            ),
            name="platform",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "w-full p-2 mb-3 bg-[#2a2a2a] text-[#F5F5F5] border border-[#333333] rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
                "w-full p-2 mb-3 bg-white text-black border border-gray-300 rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
            ),
        ),
        rx.el.label(
            "Due Date:",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "block text-sm font-medium text-[#A0A0A0] mb-1",
                "block text-sm font-medium text-gray-700 mb-1",
            ),
        ),
        rx.el.input(
            name="due_date",
            type="date",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "w-full p-2 mb-3 bg-[#2a2a2a] text-[#F5F5F5] border border-[#333333] rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
                "w-full p-2 mb-3 bg-white text-black border border-gray-300 rounded-md focus:ring-[#E63946] focus:border-[#E63946]",
            ),
        ),
        rx.el.label(
            "Budget ($):",
            class_name=rx.cond(
                PrintOptimizerState.theme == "dark",
                "block text-sm font-medium text-[#A0A0A0] mb-1",
                "block text-sm font-medium text-gray-700 mb-1",
            ),
        ),
        rx.el.input(
            name="budget",
            type="number",
            placeholder="0.00",
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
                on_click=PrintOptimizerState.toggle_project_form,
                class_name=rx.cond(
                    PrintOptimizerState.theme == "dark",
                    "p-2 bg-gray-600 text-[#F5F5F5] rounded-md hover:bg-gray-500 transition-colors",
                    "p-2 bg-gray-300 text-black rounded-md hover:bg-gray-400 transition-colors",
                ),
            ),
            rx.el.button(
                "Add Project",
                type="submit",
                class_name="p-2 bg-[#E63946] text-[#F5F5F5] rounded-md hover:bg-opacity-80 transition-colors",
            ),
            class_name="flex justify-end space-x-2 mt-2",
        ),
        on_submit=PrintOptimizerState.add_project,
        reset_on_submit=True,
        class_name=rx.cond(
            PrintOptimizerState.theme == "dark",
            "p-4 bg-[#252525] rounded-lg shadow-md mb-6",
            "p-4 bg-white rounded-lg shadow-md mb-6 border border-gray-200",
        ),
    )


def project_registration() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2(
                "Project Registration",
                class_name=rx.cond(
                    PrintOptimizerState.theme == "dark",
                    "text-xl font-semibold text-[#F5F5F5]",
                    "text-xl font-semibold text-black",
                ),
            ),
            rx.el.button(
                rx.cond(
                    PrintOptimizerState.show_project_form,
                    "Close Form",
                    "Add Project",
                ),
                on_click=PrintOptimizerState.toggle_project_form,
                class_name="p-2 bg-[#E63946] text-[#F5F5F5] rounded-md hover:bg-opacity-80 transition-colors",
            ),
            class_name="flex justify-between items-center mb-4",
        ),
        rx.cond(
            PrintOptimizerState.show_project_form,
            project_form(),
        ),
        rx.el.div(
            rx.foreach(
                PrintOptimizerState.projects_data,
                project_card,
            ),
            class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4",
        ),
        rx.cond(
            PrintOptimizerState.projects_data.length() == 0,
            rx.el.p(
                "No projects registered yet.",
                class_name=rx.cond(
                    PrintOptimizerState.theme == "dark",
                    "text-center text-[#A0A0A0] py-4",
                    "text-center text-gray-500 py-4",
                ),
            ),
        ),
        class_name="mt-8",
    )