import streamlit as st
import pandas as pd
import datetime

st.set_page_config(
    page_title="In the Waiting Sanctuary Dashboard",
    page_icon="🌿",
    layout="centered",
)

st.title("🌿 In the Waiting: Sanctuary Dashboard")
st.markdown(
    "Your private anti-hustle toolkit for nervous system regulation, boundary"
    " setting, and intentional pacing."
)
st.divider()

# Create the 6 core tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Somatic Anchor",
    "Boundary Audit",
    "Rhythm Planner",
    "Vision Canvas",
    "Self-Scheduler",
    "Progress Tracker",
])

with tab1:
  st.header("Somatic Anchor & Reset Generator")
  st.write(
      "Select your current state to generate an immediate, 2-minute grounding"
      " script."
  )

  stress_level = st.slider("Current Stress/Tension Level (1-10)", 1, 10, 5)
  tension_area = st.selectbox(
      "Where are you holding the most physical tension right now?",
      ["Jaw / Teeth", "Shoulders / Neck", "Chest / Tight Breathing", "Hands"],
  )

  if st.button("Generate Somatic Script"):
    st.subheader("Your 2-Minute Grounding Protocol:")
    if stress_level > 7:
      st.info(
          f"**High Activation Detected:** Since your stress is at a"
          f" {stress_level}/10 and held in your {tension_area}, pause"
          " immediately. Drop your shoulders away from your ears. Take 4 slow"
          " breaths: inhale for 4 seconds, hold for 4, exhale slowly through"
          " pursed lips for 6. Let your jaw slacken."
      )
    elif stress_level > 4:
      st.info(
          f"**Moderate Tension:** Acknowledge the tightness in your"
          f" {tension_area}. Place one hand on your chest. Inhale deeply"
          " through your nose, filling your belly, and exhale with a gentle"
          " sigh. Repeat 3 times."
      )
    else:
      st.info(
          "**Maintenance Reset:** You are tracking well. Take one deep breath,"
          " drop your tongue from the roof of your mouth, and notice your feet"
          " grounded on the floor."
      )

with tab2:
  st.header("Daily Energy Leak & Boundary Audit")
  st.write(
      "Identify your hidden energy drains to calculate your hustle load and"
      " generate a boundary script."
  )

  drains = [
      "Saying yes to requests out of guilt or obligation",
      "Multitasking across multiple screens or projects simultaneously",
      "Answering notifications or emails outside of designated hours",
      "Carrying mental load for others without asking for shared support",
      "Skipping basic rest or meals to push through a task list",
  ]

  selected_drains = []
  for drain in drains:
    if st.checkbox(drain):
      selected_drains.append(drain)

  hustle_score = len(selected_drains)

  if st.button("Calculate Hustle Load"):
    st.metric(
        label="Hustle Load Score", value=f"{hustle_score} / 5 Drains Active"
    )
    if hustle_score >= 3:
      st.warning(
          "**High Burnout Risk:** Your nervous system is carrying an"
          " unsustainable load today."
      )
    elif hustle_score > 0:
      st.info(
          "**Moderate Load:** Minor energy leaks detected. Small adjustments will"
          " protect your space."
      )
    else:
      st.success(
          "**Clean Boundaries:** Excellent work protecting your energy today!"
      )

    st.subheader("Suggested Boundary Script:")
    st.code(
        '"Thank you for thinking of me. Right now, my bandwidth is fully'
        ' committed to protecting my current capacity, so I won\'t be able to'
        ' take this on right now."',
        language="text",
    )

with tab3:
  st.header("Anti-Hustle Rhythm Planner")
  st.write(
      "Design a sustainable, low-pressure daily rhythm centered around what"
      " actually matters."
  )

  core_priority = st.text_input(
      "What is your ONE primary focus or priority for today?",
      "Rest and complete core task",
  )
  pacing_style = st.selectbox(
      "Select your pacing style for today:",
      [
          "Gentle (Low intensity, high rest)",
          "Paced (Steady, rhythmic intervals)",
          "Restorative (Deep recovery mode)",
      ],
  )

  if st.button("Format Daily Outline"):
    st.subheader("Your Paced Daily Outline:")
    st.markdown(f"**Core Focus:** {core_priority}")
    st.markdown(f"**Selected Pacing:** {pacing_style}")
    st.markdown("---")
    st.markdown(
        "1. **Morning Grounding:** 15 minutes of quiet stillness before opening"
        " screens."
    )
    st.markdown(
        "2. **Focus Block 1:** 45 minutes of uninterrupted work on your core"
        " priority."
    )
    st.markdown(
        "3. **Midday Reset:** Step away, step outside, or use the Somatic Anchor"
        " tab."
    )
    st.markdown(
        "4. **Afternoon Wind-Down:** Close tasks by 4 PM and transition into"
        " evening rest."
    )

with tab4:
  st.header("Vision & Daydream Canvas")
  st.write(
      "Map out your future pacing and lifestyle milestones without hustle"
      " culture pressure."
  )

  ideal_pace = st.text_input(
      "Describe your ideal weekly work pace in one sentence:",
      (
          "Working three focused days a week with four days left completely"
          " open for creativity and rest."
      ),
  )
  desired_feeling = st.text_input(
      "How do you want your daily life to *feel* 12 months from now?",
      "Quiet, spacious, unhurried, and deeply grounded.",
  )
  key_milestone = st.text_input(
      "What is one major lifestyle milestone you are quietly building toward?",
      (
          "Achieving sustainable monthly recurring revenue through automated"
          " digital products and memberships."
      ),
  )

  if st.button("Synthesize Vision Summary"):
    st.subheader("Your Personalized Vision Canvas:")
    st.success(
        f"**The Blueprint:** In your next chapter, you are building a life"
        f" anchored in **{desired_feeling.lower()}**. Your rhythm will embrace"
        f" **{ideal_pace.lower()}**, moving steadily toward your milestone of"
        f" **{key_milestone.lower()}**. You are choosing sustainable"
        " creation over burnout."
    )

with tab5:
  st.header("Anti-Hustle Self-Scheduler")
  st.write(
      "Design an unhurried daily calendar with automatic rest buffers and"
      " white space."
  )

  available_hours = st.slider(
      "How many hours of energy do you realistically have today?", 2, 8, 4
  )
  st.info(
      f"Allocating **{available_hours} hours** of operating window. The rest of"
      " your day is officially reserved for white space and recovery."
  )

  if st.button("Generate White-Space Schedule"):
    st.subheader("Your Protected Schedule:")
    st.markdown(f"**9:00 AM – 9:30 AM:** Gentle Awakening & Morning Grounding")
    st.markdown(
        f"**9:30 AM – 11:30 AM:** Focus Block A (Deep work on primary priority)"
    )
    st.markdown(
        f"**11:30 AM – 1:00 PM:** *Mandatory White Space / Rest Buffer* (Lunch &"
        " Disconnect)"
    )
    if available_hours > 4:
      st.markdown(
          f"**1:00 PM – 3:00 PM:** Focus Block B (Secondary task or creative"
          " asset creation)"
      )
    st.markdown(
        f"**After {available_hours} hours total:** Hard stop. Screens closed,"
        " system offline."
    )

with tab6:
  st.header("Progress Tracker & Milestone Log")
  st.write(
      "Click your wins below to log your progress instantly with zero typing"
      " required."
  )

  col1, col2 = st.columns(2)

  with col1:
    st.subheader("Quick Log Wins")
    win_1 = st.checkbox("✨ Protected Evening Rest Time")
    win_2 = st.checkbox("🛡️ Successfully Set a Boundary")
    win_3 = st.checkbox("🎯 Completed 1 Focus Block")
    win_4 = st.checkbox("🌿 Took a Somatic Reset Break")

  with col2:
    st.subheader("Monthly Consistency Summary")
    # Simulated generic category data for visualization
    data = pd.DataFrame({
        "Category": [
            "Rest Protected",
            "Boundaries Set",
            "Focus Blocks",
            "Somatic Resets",
        ],
        "Logged Count": [
            int(win_1) * 5 + 12,
            int(win_2) * 3 + 8,
            int(win_3) * 4 + 15,
            int(win_4) * 6 + 10,
        ],
    })
    st.bar_chart(data, x="Category", y="Logged Count")
    st.caption(
        "Visualizing your cumulative anti-hustle consistency for the month."
    )
