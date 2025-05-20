import reflex as rx
from printoptimizer.states.print_optimizer_state import (
    PrintOptimizerState,
)
from printoptimizer.components.sidebar import sidebar
from printoptimizer.components.header_bar import header_bar
from printoptimizer.components.summary_panel import summary_panel
from printoptimizer.components.marketplace_integrations import (
    marketplace_integrations,
)
from printoptimizer.components.trends_chart import trends_chart
from printoptimizer.components.ai_metadata_widget import (
    ai_metadata_widget,
)
from printoptimizer.components.cost_control_panel import (
    cost_control_panel,
)
from printoptimizer.components.upload_sync_status import (
    upload_sync_status,
)
from printoptimizer.components.project_registration import (
    project_registration,
)
from printoptimizer.components.inventory_dashboard import (
    inventory_dashboard,
)
from printoptimizer.components.material_ordering import (
    material_ordering,
)
from printoptimizer.components.quotation_area import quotation_area
from printoptimizer.components.interactive_calendar import (
    interactive_calendar,
)
from printoptimizer.components.pdf_export_module import (
    pdf_export_module,
)
from printoptimizer.components.mail_inbox import mail_inbox


def main_content_area() -> rx.Component:
    return rx.el.main(
        header_bar(),
        rx.el.div(
            rx.match(
                PrintOptimizerState.active_view,
                ("summary", summary_panel()),
                (
                    "marketplaces",
                    marketplace_integrations(),
                ),
                ("trends", trends_chart()),
                ("metadata", ai_metadata_widget()),
                ("costs", cost_control_panel()),
                ("uploads", upload_sync_status()),
                ("projects", project_registration()),
                ("inventory", inventory_dashboard()),
                ("ordering", material_ordering()),
                ("quotations", quotation_area()),
                ("calendar", interactive_calendar()),
                ("pdf_export", pdf_export_module()),
                ("mail_inbox", mail_inbox()),
                rx.el.div(
                    rx.el.h2(
                        PrintOptimizerState.current_page_title,
                        class_name="text-xl font-semibold",
                    ),
                    rx.el.p(
                        "Content for this section is under development."
                    ),
                    class_name="p-6",
                ),
            ),
            class_name="p-6 overflow-y-auto",
            style={"height": "calc(100vh - 4rem)"},
        ),
        class_name=rx.cond(
            PrintOptimizerState.theme == "dark",
            "flex-1 flex flex-col bg-[#181818] text-[#A0A0A0]",
            "flex-1 flex flex-col bg-[#F0F0F0] text-[#505050]",
        ),
    )


def index() -> rx.Component:
    return rx.el.div(
        sidebar(),
        main_content_area(),
        class_name=rx.cond(
            PrintOptimizerState.theme == "dark",
            "flex h-screen w-screen bg-[#1E1E1E] text-[#F5F5F5] overflow-hidden",
            "flex h-screen w-screen bg-white text-black overflow-hidden",
        ),
    )


app = rx.App(
    theme=rx.theme(appearance="light", accent_color="red"),
    stylesheets=[
        "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.css"
    ],
)
app.add_page(index)