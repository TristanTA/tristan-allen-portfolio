---
title: "Tristan Allen"
layout: splash
permalink: /
classes: wide

# Optional: keeps the hero readable on any background.
header:
  overlay_color: "#1F2428"          # gunmetal steel (homepage only)
  overlay_filter: "0.55"            # darkens overlay_image for contrast
  overlay_image: /assets/images/hero-pattern.svg 
  actions:
    - label: "View Case Studies"
      url: "/case-studies/"
      class: "btn btn--primary"
    - label: "Resume (PDF)"
      url: "/assets/docs/Tristan_Allen_Resume.pdf"
      class: "btn btn--inverse"

excerpt: >
  **Engineering intelligent systems that enhance human decision-making and performance.**

# ---- Case Study Grid (4 highlighted) ----
# Each item links to a case study page. Repo links go inside the case study pages.
feature_row:
  - title: "LifeNotes"
    url: "/case-studies/lifenotes/"
    excerpt: "Recall improving note-taking system with LLM semantic search and storage."
    btn_label: "Learn More"
    btn_class: "btn--primary"
  - title: "Alden"
    url: "/case-studies/alden/"
    excerpt: "Flexible, multi-modal personal AI assistant for scheduling, automation, and productivity."
    btn_label: "Learn More"
    btn_class: "btn--primary"
  - title: "Compass"
    url: "/case-studies/compass/"
    excerpt: "This portfolio's ambient manager. Agentic script for inspecting GitHub repos and proposing pull requests."
    btn_label: "Learn More"
    btn_class: "btn--primary"
  - title: "Mira"
    url: "/case-studies/mira/"
    excerpt: "Local, Openclaw inspired agentic assistant."
    btn_label: "Learn More"
    btn_class: "btn--primary"

---

<!-- ============================================================
  HERO META (3 columns)
============================================================ -->
<div class="hero-meta">
  <div class="hero-meta__col">
    <div class="hero-meta__title"><strong>Focus</strong></div>
    <div class="hero-meta__text">
      Human Factors &amp; Cognitive Systems<br/>
      AI Systems &amp; Applied ML<br/>
      Data Science &amp; Research<br/>
      I/O Psychology
    </div>
  </div>

  <div class="hero-meta__col">
    <div class="hero-meta__title"><strong>Education</strong></div>
    <div class="hero-meta__text">
      B.S. I/O Psychology + Data Science Minor<br/>
      Graduating April 2026<br/>
      Idaho Falls, Idaho — Open to relocate or work remote
    </div>
  </div>

  <div class="hero-meta__col">
    <div class="hero-meta__title"><strong>Contact</strong></div>
    <div class="hero-meta__text">
      <a href="mailto:tristantravus@gmail.com">tristantravus@gmail.com</a><br/>
      <a href="https://www.linkedin.com/in/tristantallen">LinkedIn</a><br/>
      <a href="https://github.com/TristanTA">GitHub</a>
    </div>
  </div>
</div>

<!-- ============================================================
  OPEN TO WORK (explicit banner) + consulting note
============================================================ -->

**Seeking Human Factors & AI Systems roles and Internships**
{: .notice--primary}

Open for pro bono, fixed-scope, or hourly collaboration depending on fit and scope.  
If you have a project in usability, research, data analysis, applied ML, or I/O consulting, please reach out  
{: .notice--info}

<!-- ============================================================
  SELECTED CASE STUDIES (4-card grid)
  TODO: Add permalinks to real pages (when the apges are created)
============================================================ -->
## Selected Case Studies
{% include feature_row %}

<!-- ============================================================
  ABOUT (why-driven) + Resume/CV links
============================================================ -->
## About
I  grew up in a family deeply engaged in psychology and thoughtful discussion about human behavior. Early on, I became interested in questions around productivity, motivation, and how people change over time.

At the same time, I was drawn to technology. I have grown up surrounded by technology. I started to learn basic coding and developer tools.

As those interests converged, I pursued a degree in Industrial-Organizational Psychology with a minor in Data Science, aiming to bridge behavioral science with technical systems. During that process, I developed a strong interest in how well-designed technology can support behavior change, improve decision-making, and reduce cognitive friction.

My work now focuses on building AI-enabled tools that are shaped by human cognition and real-world constraints. I am particularly interested in systems that help people align daily behavior with long-term goals. Most projects here are in active development and are documented transparently with defined scope, current state, and next steps.

[Learn more about me](/about/){: .btn .btn--primary}
[Resume (PDF)](/assets/docs/Tristan_Allen_Resume.pdf){: .btn .btn--inverse}
[CV (PDF)](/assets/docs/Tristan_Allen_CV.pdf){: .btn .btn--inverse}
[Resume (Web)](/resume/){: .btn .btn--light-outline}
[CV (Web)](/cv/){: .btn .btn--light-outline}

<hr class="sep" />

<!-- ============================================================
  SKILLS SNAPSHOT (broader, grouped; no usability testing claim)
  - Keep this readable: grouped > long flat list.
  - Add usability testing later once you’ve done it and can point to artifacts.
============================================================ -->

## Skills Snapshot
**Human Factors & Research**
- Research methods (study design, measurement thinking, synthesis)
- Cognitive systems framing (workload, attention, decision support)
- Applied behavioral + I/O foundations (motivation, performance, systems fit)

**AI & Systems**
- Python-first system building
- LLM system design (prompting, routing, guardrails, reliability patterns)
- Applied ML prototyping (model selection, evaluation mindset, iteration)

**Data & Engineering**
- Data analysis & visualization mindset (cleaning → insight → action)
- SQL / structured storage basics (project-dependent)
- Git + repo workflow hygiene (docs, PR flow, automation)

<hr class="sep" />

<!-- ============================================================
  RESEARCH FOUNDATIONS (high-level for now)
  - Honest: foundations + intent, not “publications”.
  - Later: link artifacts (summaries, annotated bibliographies, experiment notes).
============================================================ -->

## Research Foundations
My projects are shaped by research questions like: *How do we reduce cognitive friction? How do we support recall? How do we turn ambiguity into action without overwhelming the user?*  
This section will expand as I publish artifacts (summaries, references, experiment logs, and evaluation results).

[Explore Research](/research/){: .btn .btn--primary}

<hr class="sep" />

<!-- ============================================================
  PROJECT PREVIEW (5 items) + link to full list
  - All projects belong in /projects/ (including highlighted case studies).
  - Each line includes: name, repo link, purpose, why, current state.
============================================================ -->

## Project Preview
A small slice of the full list. Each entry is intentionally short and honest.

1) **LifeNotes** — [GitHub](https://github.com/TristanTA)  
Purpose: recall + retrieval support through practical capture workflows.  
Why: reduce friction between “I had a thought” and “I can find it later.”  
Current state: **Active development**; case study documents scope and roadmap.

2) **Alden** — [GitHub](https://github.com/TristanTA)  
Purpose: local-first assistant logic for planning, context, and automation.  
Why: build a reliable system that helps align actions with priorities (without noise).  
Current state: **Active development**; iterating on structure and tool reliability.

3) **Compass** — [GitHub](https://github.com/TristanTA)  
Purpose: decision-support concept for turning intent into clear next actions.  
Why: reduce ambiguity and cognitive load in goal selection and follow-through.  
Current state: **MVP / evolving**; under active refinement.

4) **Mira** — [GitHub](https://github.com/TristanTA)  
Purpose: portfolio agent for audits, fixes, and PR workflows with guardrails.  
Why: scale portfolio maintenance without sacrificing quality control.  
Current state: **Prototype → MVP**; reliability and workflow simplification ongoing.

5) **(Placeholder Project #5)** — [GitHub](https://github.com/TristanTA)  
Purpose: short one-liner.  
Why: short one-liner.  
Current state: **Prototype**.

[See the full project list](/projects/){: .btn .btn--primary}

<!-- ============================================================
  FOOTER CONTACT (simple, expected, professional)
============================================================ -->

<hr class="sep" />

## Contact
Email: [tristantravus@gmail.com](mailto:tristantravus@gmail.com)  
LinkedIn: [www.linkedin.com/in/tristantallen](https://www.linkedin.com/in/tristantallen)  
GitHub: [github.com/TristanTA](https://github.com/TristanTA)

<!-- ============================================================
  NOTES FOR YOU (safe to delete)
  1) Create pages later using the permalinks referenced above:
     /case-studies/, /case-studies/lifenotes/, /about/, /research/, /projects/, etc.
  2) If /assets/images/hero-pattern.svg is missing, the hero still works.
  3) “hr.sep” will render as a normal rule unless your CSS styles it—safe either way.
============================================================ -->