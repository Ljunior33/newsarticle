import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Parse the timeline data
timeline_data = {
    "timeline_segments": [
        {"segment": "Hook/Opening", "time": "0-1 min", "description": "Grab attention with travel problem"},
        {"segment": "Problem Statement", "time": "1-2 min", "description": "Fragmented travel planning experience"},
        {"segment": "Solution Demo", "time": "2-4 min", "description": "AI + Human coordinator showcase"},
        {"segment": "Market Opportunity", "time": "4-5 min", "description": "₹122B Indian travel market"},
        {"segment": "Business Model", "time": "5-6 min", "description": "Revenue streams & pricing"},
        {"segment": "Traction & Financials", "time": "6-7 min", "description": "Projections & growth metrics"},
        {"segment": "The Ask", "time": "7-8 min", "description": "Investment amount & equity"},
        {"segment": "Closing & Q&A", "time": "8-10 min", "description": "Vision & investor questions"}
    ]
}

# Process data for timeline
segments = []
start_times = []
durations = []
colors = []

# Travel-themed colors (blues and greens as requested)
travel_colors = ['#1FB8CD', '#2E8B57', '#5D878F', '#1FB8CD', '#2E8B57', '#5D878F', '#1FB8CD', '#2E8B57']

for i, item in enumerate(timeline_data["timeline_segments"]):
    # Truncate segment names to 15 characters
    segment_name = item["segment"]
    if len(segment_name) > 15:
        if "Statement" in segment_name:
            segment_name = "Problem Stmt"
        elif "Opportunity" in segment_name:
            segment_name = "Market Opp"
        elif "Financials" in segment_name:
            segment_name = "Traction/Fin"
        elif "Closing" in segment_name:
            segment_name = "Closing/Q&A"
        else:
            segment_name = segment_name[:15]
    
    segments.append(segment_name)
    
    # Parse time range
    time_range = item["time"].replace(" min", "")
    start, end = map(int, time_range.split("-"))
    start_times.append(start)
    durations.append(end - start)
    colors.append(travel_colors[i])

# Create timeline chart using Gantt-style approach
fig = go.Figure()

for i, (segment, start, duration, color) in enumerate(zip(segments, start_times, durations, colors)):
    fig.add_trace(go.Bar(
        name=segment,
        x=[duration],
        y=[segment],
        base=[start],
        orientation='h',
        marker=dict(color=color),
        text=f"{start}-{start+duration}min",
        textposition="inside",
        textfont=dict(color="white", size=11),
        hovertemplate=f"<b>{segment}</b><br>Time: {start}-{start+duration} min<br><extra></extra>"
    ))

# Update layout
fig.update_layout(
    title="Travel Tailor Pitch Timeline",
    xaxis_title="Time (min)",
    yaxis_title="Segments",
    showlegend=False,
    xaxis=dict(range=[0, 10], tickmode='linear', tick0=0, dtick=1),
    yaxis=dict(categoryorder='array', categoryarray=segments[::-1])  # Reverse to show first segment at top
)

fig.update_traces(cliponaxis=False)

# Save as both PNG and SVG
fig.write_image("chart.png")
fig.write_image("chart.svg", format="svg")

fig.show()