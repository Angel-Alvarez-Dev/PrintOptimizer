import reflex as rx
from printoptimizer.states.print_optimizer_state import (
    PrintOptimizerState,
)
from printoptimizer.components.kpi_card import kpi_card


def summary_panel() -> rx.Component:
    return rx.el.div(
        kpi_card(
            title="Active Projects",
            value=PrintOptimizerState.kpi_data[
                "active_projects"
            ],
            icon_name="briefcase",
        ),
        kpi_card(
            title="Total Revenue",
            value=PrintOptimizerState.kpi_data[
                "total_revenue"
            ],
            icon_name="dollar-sign",
            value_prefix="$",
        ),
        kpi_card(
            title="Average Cost",
            value=PrintOptimizerState.kpi_data[
                "average_cost"
            ],
            icon_name="bar-chart-3",
            value_prefix="$",
        ),
        kpi_card(
            title="Profit Margin",
            value=PrintOptimizerState.kpi_data[
                "profit_margin"
            ],
            icon_name="pie-chart",
            value_suffix="%",
        ),
        class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6",
    )