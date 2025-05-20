import reflex as rx
from typing import (
    TypedDict,
    Literal,
    List,
    Dict,
    Any,
    get_args,
)
import datetime
import urllib.parse

MarketplaceName = Literal[
    "Thingiverse", "MyMiniFactory", "Cults3D", "Patreon"
]
TrendPlatform = Literal[
    "All Platforms",
    "Thingiverse",
    "MyMiniFactory",
    "Cults3D",
    "Patreon",
]
TrendDateRange = Literal[
    "Last 7 Days",
    "Last 30 Days",
    "Last 90 Days",
    "All Time",
]
ProjectStatus = Literal[
    "Planning",
    "In Progress",
    "On Hold",
    "Completed",
    "Cancelled",
]
UploadStatus = Literal[
    "Pending", "Uploading", "Processing", "Synced", "Error"
]
MaterialOrderStatus = Literal[
    "Pending",
    "Ordered",
    "Shipped",
    "Delivered",
    "Cancelled",
]
CalendarEventType = Literal[
    "Upload", "Pledge", "Order", "Milestone", "General"
]
ThemeType = Literal["light", "dark"]


class KpiData(TypedDict):
    active_projects: int
    total_revenue: float
    average_cost: float
    profit_margin: float


class MarketplaceStats(TypedDict):
    name: MarketplaceName
    views: int
    downloads: int
    pledges: int | None
    revenue: float
    payment_methods: List[str]


class DesignEntry(TypedDict):
    id: int
    name: str
    description: str
    file_path: str | None
    platform: MarketplaceName | Literal["Manual"]


class TrendDataPoint(TypedDict):
    month: str
    sales: float
    downloads: int


class AiMetadata(TypedDict):
    title: str
    description: str
    tags: List[str]


class CostItem(TypedDict):
    name: str
    cost_per_unit: float
    unit: str
    quantity: float
    file_type: str
    client_project_name: str


class UploadItem(TypedDict):
    name: str
    type: Literal[".STL", ".3MF", "Patreon Release"]
    progress: int
    status: UploadStatus


class ProjectEntry(TypedDict):
    id: int
    name: str
    client: str
    platform: MarketplaceName | Literal["Direct"]
    due_date: str
    budget: float
    status: ProjectStatus


class InventoryItem(TypedDict):
    name: str
    stock_level: float
    unit: str
    low_stock_threshold: float
    reorder_threshold: float


class MaterialOrder(TypedDict):
    id: int
    supplier: str
    items: Dict[str, int]
    expected_delivery: str
    status: MaterialOrderStatus


class QuoteItem(TypedDict):
    id: int
    description: str
    quantity: int
    unit_price: float


class Quote(TypedDict):
    id: int
    client_name: str
    items: List[QuoteItem]
    markup_percentage: float
    date_created: str


class CalendarEvent(TypedDict):
    id: int
    title: str
    start: str
    end: str
    color: str
    type: CalendarEventType


class MailMessage(TypedDict):
    id: int
    sender: str
    subject: str
    body: str
    received_at: str
    processed: bool


class PrintOptimizerState(rx.State):
    sidebar_collapsed: bool = False
    active_view: str = "summary"
    theme: ThemeType = "dark"
    next_calendar_event_id: int = 3
    next_mail_id: int = 1
    next_manual_design_id: int = 1
    next_quote_id: int = 1
    next_quote_item_id: int = 1
    kpi_data: KpiData = {
        "active_projects": 12,
        "total_revenue": 8250.0,
        "average_cost": 14.85,
        "profit_margin": 32.5,
    }
    marketplace_data: List[MarketplaceStats] = [
        {
            "name": "Thingiverse",
            "views": 2100,
            "downloads": 480,
            "pledges": None,
            "revenue": 1500.0,
            "payment_methods": ["PayPal"],
        },
        {
            "name": "MyMiniFactory",
            "views": 1780,
            "downloads": 640,
            "pledges": None,
            "revenue": 2300.0,
            "payment_methods": ["Card"],
        },
        {
            "name": "Cults3D",
            "views": 1200,
            "downloads": 300,
            "pledges": None,
            "revenue": 1800.0,
            "payment_methods": ["PayPal", "Card"],
        },
        {
            "name": "Patreon",
            "views": 300,
            "downloads": 0,
            "pledges": 150,
            "revenue": 2650.0,
            "payment_methods": ["Card", "Crypto"],
        },
    ]
    manually_added_designs: List[DesignEntry] = []
    show_add_design_form: bool = False
    trends_chart_data: List[TrendDataPoint] = [
        {"month": "Jan", "sales": 200, "downloads": 50},
        {"month": "Feb", "sales": 180, "downloads": 60},
        {"month": "Mar", "sales": 220, "downloads": 70},
        {"month": "Apr", "sales": 300, "downloads": 80},
        {"month": "May", "sales": 280, "downloads": 90},
        {"month": "Jun", "sales": 350, "downloads": 100},
        {"month": "Jul", "sales": 400, "downloads": 120},
        {"month": "Aug", "sales": 380, "downloads": 110},
    ]
    selected_trend_platform: TrendPlatform = "All Platforms"
    selected_trend_date_range: TrendDateRange = (
        "Last 30 Days"
    )
    hovered_trend_data: TrendDataPoint | None = None
    ai_metadata: AiMetadata = {
        "title": "",
        "description": "",
        "tags": [],
    }
    cost_control_data: List[CostItem] = [
        {
            "name": "Filament",
            "cost_per_unit": 20.0,
            "unit": "/kg",
            "quantity": 1.5,
            "file_type": ".STL",
            "client_project_name": "Client A Model",
        },
        {
            "name": "Resin",
            "cost_per_unit": 50.0,
            "unit": "/L",
            "quantity": 0.75,
            "file_type": ".3MF",
            "client_project_name": "Internal Project X",
        },
        {
            "name": "Power",
            "cost_per_unit": 0.12,
            "unit": "/kWh",
            "quantity": 10.0,
            "file_type": "N/A",
            "client_project_name": "Overhead",
        },
        {
            "name": "Labor",
            "cost_per_unit": 8.0,
            "unit": "/hr",
            "quantity": 2.5,
            "file_type": "N/A",
            "client_project_name": "Client A Model",
        },
    ]
    cost_control_expanded: bool = True
    uploads_data: List[UploadItem] = [
        {
            "name": "Gadget Prototype",
            "type": ".STL",
            "progress": 100,
            "status": "Synced",
        },
        {
            "name": "Character Figurine",
            "type": ".3MF",
            "progress": 75,
            "status": "Uploading",
        },
        {
            "name": "Puzzle Model",
            "type": ".STL",
            "progress": 0,
            "status": "Pending",
        },
        {
            "name": "Decorative Vase",
            "type": "Patreon Release",
            "progress": 10,
            "status": "Error",
        },
    ]
    projects_data: List[ProjectEntry] = [
        {
            "id": 1,
            "name": "Client A Model",
            "client": "Client A",
            "platform": "Direct",
            "due_date": "2024-08-15",
            "budget": 500,
            "status": "In Progress",
        },
        {
            "id": 2,
            "name": "Thingiverse Upload",
            "client": "Internal",
            "platform": "Thingiverse",
            "due_date": "2024-09-01",
            "budget": 100,
            "status": "Planning",
        },
    ]
    show_project_form: bool = False
    inventory_data: List[InventoryItem] = [
        {
            "name": "PLA Filament (Black)",
            "stock_level": 5.5,
            "unit": "kg",
            "low_stock_threshold": 2.0,
            "reorder_threshold": 1.0,
        },
        {
            "name": "ABS Resin (Grey)",
            "stock_level": 2.0,
            "unit": "L",
            "low_stock_threshold": 1.0,
            "reorder_threshold": 0.5,
        },
    ]
    material_orders_data: List[MaterialOrder] = []
    quotes_data: List[Quote] = []
    current_quote_items: List[QuoteItem] = []
    current_quote_client_name: str = ""
    current_quote_markup_percentage: float = 0.0
    new_quote_item_description: str = ""
    new_quote_item_quantity: int = 1
    new_quote_item_unit_price: float = 0.0
    calendar_events_data: List[CalendarEvent] = [
        {
            "id": 1,
            "title": "Upload Gadget Prototype",
            "start": "2024-07-20",
            "end": "2024-07-20",
            "color": "#3182CE",
            "type": "Upload",
        },
        {
            "id": 2,
            "title": "Patreon Pledge Cycle",
            "start": "2024-08-01",
            "end": "2024-08-01",
            "color": "#E53E3E",
            "type": "Pledge",
        },
    ]
    mail_inbox_data: List[MailMessage] = []
    show_add_calendar_event_form: bool = False

    @rx.var
    def current_page_title(self) -> str:
        titles = {
            "summary": "Summary",
            "marketplaces": "Marketplace Integrations",
            "trends": "Performance Trends",
            "metadata": "AI Metadata Generator",
            "costs": "Cost Control Panel",
            "uploads": "Upload & Sync Status",
            "projects": "Project Registration",
            "inventory": "Inventory Dashboard",
            "ordering": "Material Ordering",
            "quotations": "Quotation Area",
            "calendar": "Interactive Calendar",
            "pdf_export": "PDF Export Module",
            "mail_inbox": "Mail Inbox",
        }
        return titles.get(self.active_view, "Dashboard")

    @rx.var
    def total_cost_control_value(self) -> float:
        total = 0.0
        for item in self.cost_control_data:
            total += (
                item["cost_per_unit"] * item["quantity"]
            )
        return total

    @rx.var
    def current_quote_subtotal(self) -> float:
        return sum(
            (
                item["quantity"] * item["unit_price"]
                for item in self.current_quote_items
            )
        )

    @rx.var
    def current_quote_markup_amount(self) -> float:
        return self.current_quote_subtotal * (
            self.current_quote_markup_percentage / 100
        )

    @rx.var
    def current_quote_total(self) -> float:
        return (
            self.current_quote_subtotal
            + self.current_quote_markup_amount
        )

    @rx.var
    def quote_text_for_messaging(self) -> str:
        text = f"Quote for: {self.current_quote_client_name or 'Client'}\n\nItems:\n"
        for item in self.current_quote_items:
            text += f"- {item['description']}: {item['quantity']} x ${item['unit_price']:.2f} = ${item['quantity'] * item['unit_price']:.2f}\n"
        text += f"\nSubtotal: ${self.current_quote_subtotal:.2f}\n"
        if self.current_quote_markup_percentage > 0:
            text += f"Markup ({self.current_quote_markup_percentage}%): ${self.current_quote_markup_amount:.2f}\n"
        text += (
            f"Total: ${self.current_quote_total:.2f}\n\n"
        )
        text += "Generated by PrintOptimizer"
        return text

    @rx.var
    def whatsapp_link(self) -> str:
        phone_number = "1234567890"
        message = self.quote_text_for_messaging
        encoded_message = urllib.parse.quote_plus(message)
        return f"https://wa.me/{phone_number}?text={encoded_message}"

    @rx.var
    def gmail_link(self) -> str:
        recipient_email = ""
        subject = f"Quotation for {self.current_quote_client_name or 'Project'}"
        body = self.quote_text_for_messaging
        encoded_subject = urllib.parse.quote_plus(subject)
        encoded_body = urllib.parse.quote_plus(body)
        return f"mailto:{recipient_email}?subject={encoded_subject}&body={encoded_body}"

    @rx.event
    def toggle_sidebar(self):
        self.sidebar_collapsed = not self.sidebar_collapsed

    @rx.event
    def set_active_view(self, view: str):
        self.active_view = view
        yield rx.toast.info(
            f"Navigated to {self.current_page_title}"
        )

    @rx.event
    def generate_metadata(self):
        self.ai_metadata = AiMetadata(
            title="AI Generated Title for Model",
            description="This is an AI generated description that is SEO friendly.",
            tags=["3dprint", "model", "ai", "seo"],
        )
        yield rx.toast.success("Metadata generated!")

    @rx.event
    def toggle_cost_control_expansion(self):
        self.cost_control_expanded = (
            not self.cost_control_expanded
        )

    @rx.event
    def retry_upload(self, upload_name: str):
        yield rx.toast.info(
            f"Retrying upload for {upload_name}..."
        )

    @rx.event
    def toggle_project_form(self):
        self.show_project_form = not self.show_project_form

    @rx.event
    def add_project(self, form_data: dict):
        if not form_data.get("name") or not form_data.get(
            "due_date"
        ):
            yield rx.toast.error(
                "Project name and due date are required."
            )
            return
        new_id = (
            max([p["id"] for p in self.projects_data] + [0])
            + 1
        )
        new_project: ProjectEntry = {
            "id": new_id,
            "name": form_data["name"],
            "client": form_data.get("client", "N/A"),
            "platform": form_data.get("platform", "Direct"),
            "due_date": form_data["due_date"],
            "budget": float(form_data.get("budget", 0)),
            "status": "Planning",
        }
        self.projects_data.append(new_project)
        self.show_project_form = False
        yield rx.toast.success(
            f"Project '{new_project['name']}' added."
        )

    @rx.event
    def export_pdf_report(self):
        yield rx.toast.success(
            "Report exported successfully! (Placeholder)"
        )

    @rx.event
    def export_cost_control_pdf(self):
        yield rx.toast.info(
            "Cost control data PDF export initiated (Placeholder)."
        )

    @rx.event
    def toggle_theme(self):
        if self.theme == "light":
            self.theme = "dark"
        else:
            self.theme = "light"
        yield rx.toast.info(
            f"Theme changed to {self.theme} mode."
        )

    @rx.event
    def handle_trend_chart_hover(self):
        self.hovered_trend_data = None

    @rx.event
    def update_cost_item_cost_per_unit(
        self, item_name: str, new_cost_str: str
    ):
        try:
            new_cost = float(new_cost_str)
            if new_cost < 0:
                yield rx.toast.error(
                    f"Cost per unit for {item_name} cannot be negative."
                )
                return
            for item in self.cost_control_data:
                if item["name"] == item_name:
                    item["cost_per_unit"] = new_cost
                    break
            yield rx.toast.success(
                f"Cost per unit for {item_name} updated."
            )
        except ValueError:
            yield rx.toast.error(
                f"Invalid cost value '{new_cost_str}' for {item_name}."
            )

    @rx.event
    def update_cost_item_quantity(
        self, item_name: str, new_quantity_str: str
    ):
        try:
            new_quantity = float(new_quantity_str)
            if new_quantity < 0:
                yield rx.toast.error(
                    f"Quantity for {item_name} cannot be negative."
                )
                return
            for item in self.cost_control_data:
                if item["name"] == item_name:
                    item["quantity"] = new_quantity
                    break
            yield rx.toast.success(
                f"Quantity for {item_name} updated."
            )
        except ValueError:
            yield rx.toast.error(
                f"Invalid quantity value '{new_quantity_str}' for {item_name}."
            )

    @rx.event
    def add_sample_mail(self):
        mail_id = self.next_mail_id
        self.next_mail_id += 1
        sample_mails = [
            {
                "sender": "system@example.com",
                "subject": "ADD EVENT: Team Meeting | 2024-09-10 | Meeting | #FF5733",
                "body": "Please add a team meeting to the calendar for September 10th, 2024.",
            },
            {
                "sender": "client@example.com",
                "subject": "REMOVE EVENT ID: 1",
                "body": "Please remove the event with ID 1 (Upload Gadget Prototype).",
            },
            {
                "sender": "project_manager@example.com",
                "subject": "ADD EVENT: Project Deadline | 2024-10-01 | Milestone | #C70039",
                "body": "Add a milestone for project deadline on October 1st.",
            },
        ]
        new_mail_content = sample_mails[
            (mail_id - 1) % len(sample_mails)
        ]
        new_mail: MailMessage = {
            "id": mail_id,
            "sender": new_mail_content["sender"],
            "subject": new_mail_content["subject"],
            "body": new_mail_content["body"],
            "received_at": "2024-07-30 10:00:00",
            "processed": False,
        }
        self.mail_inbox_data.append(new_mail)
        yield rx.toast.info("Sample mail received.")

    @rx.event
    def process_mail(self, mail_id: int):
        mail_to_process = next(
            (
                m
                for m in self.mail_inbox_data
                if m["id"] == mail_id
            ),
            None,
        )
        if (
            not mail_to_process
            or mail_to_process["processed"]
        ):
            yield rx.toast.warning(
                "Mail not found or already processed."
            )
            return
        subject = mail_to_process["subject"].upper()
        processed_action = False
        if "ADD EVENT:" in subject:
            try:
                parts = (
                    mail_to_process["subject"]
                    .split(":")[1]
                    .split("|")
                )
                title = parts[0].strip()
                start_date = parts[1].strip()
                event_type_str = (
                    parts[2].strip().capitalize()
                )
                event_type: CalendarEventType = "General"
                if event_type_str in get_args(
                    CalendarEventType
                ):
                    event_type = event_type_str
                color = (
                    parts[3].strip()
                    if len(parts) > 3
                    else "#3182CE"
                )
                new_event_id = self.next_calendar_event_id
                self.next_calendar_event_id += 1
                new_event: CalendarEvent = {
                    "id": new_event_id,
                    "title": title,
                    "start": start_date,
                    "end": start_date,
                    "color": color,
                    "type": event_type,
                }
                self.calendar_events_data.append(new_event)
                yield rx.toast.success(
                    f"Event '{title}' added from mail."
                )
                processed_action = True
            except Exception as e:
                yield rx.toast.error(
                    f"Error parsing ADD EVENT mail: {str(e)}"
                )
        elif "REMOVE EVENT ID:" in subject:
            try:
                event_id_to_remove_str = (
                    mail_to_process["subject"]
                    .split(":")[1]
                    .strip()
                )
                event_id_to_remove = int(
                    event_id_to_remove_str
                )
                initial_len = len(self.calendar_events_data)
                self.calendar_events_data = [
                    event
                    for event in self.calendar_events_data
                    if event["id"] != event_id_to_remove
                ]
                if (
                    len(self.calendar_events_data)
                    < initial_len
                ):
                    yield rx.toast.success(
                        f"Event with ID {event_id_to_remove} removed from mail."
                    )
                    processed_action = True
                else:
                    yield rx.toast.warning(
                        f"Event with ID {event_id_to_remove} not found."
                    )
            except ValueError:
                yield rx.toast.error(
                    "Invalid event ID format in REMOVE EVENT mail."
                )
            except Exception as e:
                yield rx.toast.error(
                    f"Error parsing REMOVE EVENT ID mail: {str(e)}"
                )
        elif "REMOVE EVENT:" in subject:
            try:
                title_to_remove = (
                    mail_to_process["subject"]
                    .split(":")[1]
                    .strip()
                )
                initial_len = len(self.calendar_events_data)
                self.calendar_events_data = [
                    event
                    for event in self.calendar_events_data
                    if event["title"].lower()
                    != title_to_remove.lower()
                ]
                if (
                    len(self.calendar_events_data)
                    < initial_len
                ):
                    yield rx.toast.success(
                        f"Event(s) titled '{title_to_remove}' removed from mail."
                    )
                    processed_action = True
                else:
                    yield rx.toast.warning(
                        f"No event titled '{title_to_remove}' found."
                    )
            except Exception as e:
                yield rx.toast.error(
                    f"Error parsing REMOVE EVENT mail: {str(e)}"
                )
        if processed_action:
            for m_idx, m_val in enumerate(
                self.mail_inbox_data
            ):
                if m_val["id"] == mail_id:
                    self.mail_inbox_data[m_idx][
                        "processed"
                    ] = True
                    break
        else:
            yield rx.toast.info(
                "Mail subject did not match known calendar actions."
            )

    @rx.event
    def toggle_add_calendar_event_form(self):
        self.show_add_calendar_event_form = (
            not self.show_add_calendar_event_form
        )

    @rx.event
    def add_calendar_event_manually(self, form_data: dict):
        title = form_data.get("title")
        start_date = form_data.get("start_date")
        event_type_str = form_data.get(
            "event_type", "General"
        )
        if not title or not start_date:
            yield rx.toast.error(
                "Title and Start Date are required."
            )
            return
        event_type: CalendarEventType = "General"
        if event_type_str in get_args(CalendarEventType):
            event_type = event_type_str
        new_event_id = self.next_calendar_event_id
        self.next_calendar_event_id += 1
        new_event: CalendarEvent = {
            "id": new_event_id,
            "title": title,
            "start": start_date,
            "end": form_data.get("end_date", start_date),
            "color": form_data.get("color", "#3182CE"),
            "type": event_type,
        }
        self.calendar_events_data.append(new_event)
        self.show_add_calendar_event_form = False
        yield rx.toast.success(
            f"Event '{title}' added manually."
        )

    @rx.event
    def remove_calendar_event_by_id(self, event_id: int):
        self.calendar_events_data = [
            event
            for event in self.calendar_events_data
            if event["id"] != event_id
        ]
        yield rx.toast.success(
            f"Event with ID {event_id} removed."
        )

    @rx.event
    def toggle_add_design_form(self):
        self.show_add_design_form = (
            not self.show_add_design_form
        )

    @rx.event
    def add_manual_design(self, form_data: dict):
        name = form_data.get("name", "").strip()
        if not name:
            yield rx.toast.error("Design name is required.")
            return
        new_design: DesignEntry = {
            "id": self.next_manual_design_id,
            "name": name,
            "description": form_data.get("description", ""),
            "file_path": None,
            "platform": "Manual",
        }
        self.manually_added_designs.append(new_design)
        self.next_manual_design_id += 1
        self.show_add_design_form = False
        yield rx.toast.success(
            f"Design '{name}' added manually."
        )

    @rx.event
    def set_new_quote_item_description(self, value: str):
        self.new_quote_item_description = value

    @rx.event
    def set_new_quote_item_quantity(self, value: str):
        try:
            self.new_quote_item_quantity = int(value)
            if self.new_quote_item_quantity < 1:
                self.new_quote_item_quantity = 1
        except ValueError:
            self.new_quote_item_quantity = 1
            yield rx.toast.error(
                "Invalid quantity. Must be a number."
            )

    @rx.event
    def set_new_quote_item_unit_price(self, value: str):
        try:
            self.new_quote_item_unit_price = float(value)
            if self.new_quote_item_unit_price < 0:
                self.new_quote_item_unit_price = 0.0
        except ValueError:
            self.new_quote_item_unit_price = 0.0
            yield rx.toast.error(
                "Invalid unit price. Must be a number."
            )

    @rx.event
    def add_item_to_current_quote(self):
        if not self.new_quote_item_description:
            yield rx.toast.error(
                "Item description cannot be empty."
            )
            return
        if self.new_quote_item_quantity <= 0:
            yield rx.toast.error(
                "Item quantity must be greater than 0."
            )
            return
        if self.new_quote_item_unit_price < 0:
            yield rx.toast.error(
                "Item unit price cannot be negative."
            )
            return
        new_item: QuoteItem = {
            "id": self.next_quote_item_id,
            "description": self.new_quote_item_description,
            "quantity": self.new_quote_item_quantity,
            "unit_price": self.new_quote_item_unit_price,
        }
        self.current_quote_items.append(new_item)
        self.next_quote_item_id += 1
        self.new_quote_item_description = ""
        self.new_quote_item_quantity = 1
        self.new_quote_item_unit_price = 0.0
        yield rx.toast.success("Item added to quote.")

    @rx.event
    def update_current_quote_item_quantity(
        self, item_id: int, quantity_str: str
    ):
        try:
            quantity = int(quantity_str)
            if quantity <= 0:
                yield rx.toast.error(
                    "Quantity must be positive."
                )
                return
            for i, item in enumerate(
                self.current_quote_items
            ):
                if item["id"] == item_id:
                    self.current_quote_items[i][
                        "quantity"
                    ] = quantity
                    yield rx.toast.success(
                        "Item quantity updated."
                    )
                    return
            yield rx.toast.error(
                "Item not found to update quantity."
            )
        except ValueError:
            yield rx.toast.error("Invalid quantity.")

    @rx.event
    def remove_item_from_current_quote(self, item_id: int):
        self.current_quote_items = [
            item
            for item in self.current_quote_items
            if item["id"] != item_id
        ]
        yield rx.toast.info("Item removed from quote.")

    @rx.event
    def set_current_quote_client_name(self, name: str):
        self.current_quote_client_name = name

    @rx.event
    def set_current_quote_markup_percentage(
        self, markup_str: str
    ):
        try:
            markup = float(markup_str)
            if markup < 0:
                markup = 0.0
            self.current_quote_markup_percentage = markup
        except ValueError:
            self.current_quote_markup_percentage = 0.0
            yield rx.toast.error(
                "Invalid markup percentage."
            )

    @rx.event
    def save_current_quote(self):
        if not self.current_quote_items:
            yield rx.toast.error(
                "Cannot save an empty quote."
            )
            return
        new_quote: Quote = {
            "id": self.next_quote_id,
            "client_name": self.current_quote_client_name
            or f"Quote #{self.next_quote_id}",
            "items": list(self.current_quote_items),
            "markup_percentage": self.current_quote_markup_percentage,
            "date_created": datetime.datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
        }
        self.quotes_data.append(new_quote)
        self.next_quote_id += 1
        yield PrintOptimizerState.clear_current_quote
        yield rx.toast.success(
            f"Quote #{new_quote['id']} saved."
        )

    @rx.event
    def clear_current_quote(self):
        self.current_quote_items = []
        self.current_quote_client_name = ""
        self.current_quote_markup_percentage = 0.0
        self.new_quote_item_description = ""
        self.new_quote_item_quantity = 1
        self.new_quote_item_unit_price = 0.0
        yield rx.toast.info("Current quote cleared.")

    @rx.event
    def send_quote_via_whatsapp(self):
        if not self.current_quote_items:
            yield rx.toast.error(
                "Cannot send an empty quote."
            )
            return
        yield rx.toast.info("Opening WhatsApp...")

    @rx.event
    def send_quote_via_gmail(self):
        if not self.current_quote_items:
            yield rx.toast.error(
                "Cannot send an empty quote."
            )
            return
        yield rx.toast.info("Opening Gmail...")