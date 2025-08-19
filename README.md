# 🎭 The NextWord Predictor Using LSTM GRU

Predict the **next word** in Shakespeare’s *Hamlet* using two recurrent architectures—**LSTM** and **GRU**—and compare how they behave. Built for clarity, speed, and fun experimentation.

> *“Goodnight, sweet Prince…”* — Yep, the corpus is **Hamlet (public domain)**, and that’s our playground. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

---

## 🔥 Highlights

- **Two model families:** Long Short-Term Memory (**LSTM**) and Gated Recurrent Unit (**GRU**)
- **Side-by-side training** in notebooks + **one-click inference** in a Streamlit app  
- **Plug-and-play assets:** saved model(s) + tokenizer for instant use
- **Reproducible stack:** pinned core libs in `requirements.txt` (TensorFlow, Streamlit, NLTK, etc.) :contentReference[oaicite:2]{index=2}
- **Shakespearean flavor:** trained on *Hamlet* (full text included) :contentReference[oaicite:3]{index=3}

---

## 🗂️ Repository Structure

1. LSTM_RNN(Predicting_Next_Word).ipynb        # LSTM training & evaluation notebook
2. GRU_LSTM_RNN(Predicting_Next_Word).ipynb    # GRU training & evaluation notebook
3. hamlet.txt                                  # Dataset (public domain Shakespeare)
4. app.py                                      # Streamlit app (loads saved model + tokenizer)
5. next_word_lstm.h5                           # Saved LSTM model (training artifact)
6. next_word_GRU_lstm.h5                       # Saved GRU/LSTM model used by app
7. tokenizer.pickle                            # Fitted tokenizer
8. requirements.txt                            # Dependencies (TF, Streamlit, NLTK, etc.)



> The Streamlit app loads `next_word_GRU_lstm.h5` and `tokenizer.pickle` at startup

---

## 🚀 Quickstart

### 1) Clone & install
git clone https://github.com/pahul1712/The-NextWord-Predictor-Using-LSTM-GRU.git
cd The-NextWord-Predictor-Using-LSTM-GRU
pip install -r requirements.txt


2) Run the app
   
streamlit run app.py



## 🧠 How It Works (Conceptual)

1. Dataset → Sequences

Clean Shakespeare’s Hamlet, tokenize, then build next-word training pairs (N-gram sequences).

The final token index is the target; the preceding tokens form the input window.

2. Model Families

LSTM: excels at longer dependencies with memory cells.

GRU: leaner, often trains faster with comparable quality.

3. Training & Saving

Train each model in its respective notebook, monitor loss, save the best .h5 weights and tokenizer.pickle.

4. Inference (App)

Take a user prompt → tokenize → pad/truncate to the model’s input length → predict class index → map back to word.

See predict_word() and model loading in app.py. 
 

## 🧪 Try These Prompts

To be or not → model predicts …

There is nothing → model predicts …

The play's the → model predicts …
