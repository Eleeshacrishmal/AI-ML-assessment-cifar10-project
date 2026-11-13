# CIFAR-10 Assessment Work

## Project layout

- `notebooks/Exercise_1_MLP.ipynb` — three-layer MLP baseline.
- `notebooks/Exercise_2_CNN.ipynb` — three-layer CNN baseline, comparisons, and pixel-shuffle investigation.
- `notebooks/Exercise_3_Regularisation.ipynb` — baseline, dropout, augmentation, and combined regularisation experiments across three seeds.
- `notebooks/Exercise_4_CNN_Width_Depth.ipynb` — six width and depth configurations across three seeds.
- `data/` — local CIFAR-10 files. The notebooks download CIFAR-10 automatically only when it is not already present.
- `artifacts/exercise_1/` through `artifacts/exercise_4/` — checkpoints, metrics, tables, and figures for each exercise.
- `requirements.txt` — pinned versions from the verified project environment.

## Environment

Use the project `.venv` with Python 3.11 and a CUDA-enabled PyTorch build. The recorded environment uses PyTorch 2.14.1+cu126 and torchvision 0.29.1+cu126. Install the requirements in that environment. For PyTorch CUDA wheels, use the matching official PyTorch wheel index if pip does not resolve the `+cu126` builds from the default index. Select the `.venv` Jupyter kernel before running the notebooks.

## Run order

Run each notebook from top to bottom in a fresh kernel, in this order:

1. `Exercise_1_MLP.ipynb`
2. `Exercise_2_CNN.ipynb`
3. `Exercise_3_Regularisation.ipynb`
4. `Exercise_4_CNN_Width_Depth.ipynb`

Exercise 2 reads the Exercise 1 results. Exercises 3 and 4 read the Exercise 2 results. Exercise 4 loads the saved experiment runs and does not train them again. It does not load the official test set.

## Reproducibility and data

The exercises use CIFAR-10 normalization with channel means `(0.4914, 0.4822, 0.4465)` and standard deviations `(0.2470, 0.2435, 0.2616)`, a seed-42 45,000/5,000 training/validation split, batch size 64, Adam with learning rate `0.001`, and 20 epochs. The test partition is reserved for final evaluation in Exercises 1–3. Exercise 4 uses only training and validation data. Results and plots are written below `artifacts/`.

The additional investigations are labelled in the notebooks: Exercise 2 studies pixel shuffling; Exercise 3 includes a dropout-plus-augmentation combined run. These are reported separately from the primary comparisons.

## Runtime

On the RTX 3050 Laptop GPU, the completed Exercise 1 run took about 4.2 minutes. Exercise 2, including the pixel-shuffle investigation, took about 15.7 minutes. Exercise 3 runs 12 trainings (four conditions × three seeds) and took about 66 minutes of measured training time. Exercise 4 loads 18 saved runs (six configurations × three seeds) in about 42 seconds; their original training took about 77 minutes in total. Runtime depends on system load and data-loader throughput.

To shorten exploratory runs, change `EPOCHS` or `SEEDS` in a notebook's configuration cell, then rerun it from the top. Reduced-run results are not directly comparable with the full 20-epoch, three-seed results.
