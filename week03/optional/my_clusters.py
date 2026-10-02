"""Week 3 · Optional: cluster a corpus (Semantics Exercise 6).

Put nine or ten sentences from three topics you know well in `corpus`, plus one
`straddler` that belongs to two of them. Run from the week03 folder:
    uv run optional/my_clusters.py
"""
import numpy as np
from sklearn.cluster import KMeans
from genai import embed

corpus = [                                                   # ← your sentences
    "Neural networks learn patterns from data",
    "Machine learning powers modern AI systems",
    "Deep learning models can recognize images",
    "The chef simmered the tomato sauce for an hour",
    "Fresh basil and garlic make the pasta fragrant",
    "Bakers knead dough to develop gluten",
    "The telescope captured a distant spiral galaxy",
    "Astronauts orbited the Earth for six months",
    "A rocket launched toward the moon at dawn",
]
straddler = "Dissolve the yeast in warm water, then measure the reaction rate"   # ← yours

docs = corpus + [straddler]
vecs = np.array([embed(d) for d in docs])
labels = KMeans(n_clusters=3, random_state=42, n_init=10).fit_predict(vecs)
for doc, lab in sorted(zip(docs, labels), key=lambda x: x[1]):
    mark = "  ← straddler" if doc == straddler else ""
    print(f"[{lab}] {doc}{mark}")
