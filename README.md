
# 🏷️ Auto-Tagging-Support-Tickets-Using-LLM

## 📌 Project Overview

This project is **Auto Tagging Support Tickets Using LLM**.
The aim of this project is to automatically classify and tag customer support tickets into relevant categories using a **Large Language Model (LLM)**.

Instead of traditional rule-based systems, this project uses **LLM-powered text understanding** to generate accurate and meaningful tags from free-text tickets.

---

## 🎯 Objective

To build an intelligent system that can:

* Understand free-text support tickets
* Assign the **top 3 most relevant tags** to each ticket
* Compare different LLM-based classification approaches

---

## 📂 Dataset

* **Free-text Support Ticket Dataset**
* Contains real or simulated customer issues written in natural language
* Tickets may belong to multiple categories such as billing, login issues, technical errors, or account management

---

## 🛠️ Project Tasks

The following steps are implemented in this project:

* Using **prompt engineering** to classify tickets with an LLM
* Applying **zero-shot learning** for baseline performance
* Applying **few-shot learning** to improve classification accuracy
* (Optional) Fine-tuning an LLM for task-specific performance
* Generating and ranking the **top 3 most probable tags** for each ticket

---

## 🔍 Zero-Shot vs Few-Shot Learning

* **Zero-shot learning**:

  * The model predicts tags without seeing labeled examples
  * Fast and cost-effective
* **Few-shot learning**:

  * The model is given a small number of labeled examples in the prompt
  * Improves accuracy and consistency

Performance from both approaches is compared and analyzed.

---

## 🏷️ Output Format

For each support ticket, the model outputs:

* **Top 3 predicted tags**
* Ordered by relevance and confidence

Example:

```
Ticket: "Unable to reset my password and login to my account"

Predicted Tags:
1. Account Access
2. Password Reset
3. Authentication Issue
```

---

## 🧠 Skills Gained

Through this project, the following skills were developed:

* Prompt engineering for LLMs
* LLM-based text classification
* Zero-shot and few-shot learning techniques
* Multi-class prediction and ranking

---

## 📁 Repository Structure (Optional)

```
Auto-Tagging-Support-Tickets/
│
├── data/
├── prompts/
├── notebooks/
├── tagger.py
├── requirements.txt
└── README.md
```

---

## 🧰 Tools & Technologies

* Python
* Large Language Models (LLMs)
* Prompt Engineering
* NLP Techniques

---

## ✅ Conclusion

This project demonstrates how LLMs can be effectively used for automatic support ticket tagging. It highlights the power of prompt design and few-shot learning in solving real-world text classification problems without heavy model training.


