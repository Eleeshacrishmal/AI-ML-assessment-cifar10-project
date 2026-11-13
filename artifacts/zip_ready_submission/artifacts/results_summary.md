# CIFAR-10 Assessment: Results Summary

Generated from the saved exercise result files.

## Exercise 1 — MLP

| Checkpoint | Train accuracy | Validation accuracy | Test accuracy | Train loss | Validation loss | Test loss | Parameters |
|---|---:|---:|---:|---:|---:|---:|---:|
| Final epoch | 84.23% | 51.68% | 51.65% | 0.4464 | 2.2189 | 2.1902 | 1,707,274 |
| Best validation-loss checkpoint (epoch 5) | 61.25% | 50.50% | 50.90% | 1.0965 | 1.4221 | 1.4295 | 1,707,274 |

Training time: 253.2 s. Validation-loss minimum: epoch 5, 1.4221.

## Exercise 2 — CNN baseline and comparisons

| Model/checkpoint | Train accuracy | Validation accuracy | Test accuracy | Train loss | Validation loss | Test loss | Train–test gap (pp) | Parameters |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| MLP — Final epoch | 84.23% | 51.68% | 51.65% | 0.4464 | 2.2189 | 2.1902 | 32.58 | 1,707,274 |
| MLP — Best validation-loss checkpoint | 61.25% | 50.50% | 50.90% | 1.0965 | 1.4221 | 1.4295 | 10.35 | 1,707,274 |
| CNN — Final epoch | 92.09% | 67.86% | 68.50% | 0.2271 | 1.3634 | 1.3832 | 23.59 | 60,362 |
| CNN — Best validation-loss checkpoint | 83.87% | 71.40% | 71.43% | 0.4870 | 0.8440 | 0.8596 | 12.44 | 60,362 |

CNN minus MLP test accuracy: +16.85 pp at the final epoch; +20.53 pp for the best-validation-loss checkpoints.
Final CNN training time: 268.8 s. CNN validation-loss checkpoint: epoch 7.

### Pixel-shuffle investigation

| Model | Original test accuracy | Shuffled-pixel test accuracy | Change (pp) |
|---|---:|---:|---:|
| MLP | 51.65% | 51.32% | -0.33 |
| CNN | 68.50% | 47.47% | -21.03 |

## Exercise 3 — Regularisation

Mean ± sample standard deviation over the three seeds.

| Condition | Train accuracy | Validation accuracy | Test accuracy | Train–test gap (pp) | Train loss | Test loss | Parameters |
|---|---:|---:|---:|---:|---:|---:|---:|
| Baseline | 91.87% ± 0.62 pp | 68.69% ± 0.72 pp | 68.81% ± 0.49 pp | 23.06 ± 0.49 | 0.2321 ± 0.0206 | 1.3650 ± 0.0420 | 60,362 |
| Dropout | 83.81% ± 0.94 pp | 74.53% ± 0.49 pp | 73.74% ± 0.79 pp | 10.06 ± 0.19 | 0.4849 ± 0.0220 | 0.7660 ± 0.0296 | 60,362 |
| Augmentation | 77.29% ± 0.82 pp | 74.27% ± 0.83 pp | 74.63% ± 0.98 pp | 2.65 ± 0.33 | 0.6637 ± 0.0259 | 0.7472 ± 0.0276 | 60,362 |
| Dropout + Augmentation (additional combined run) | 74.97% ± 0.56 pp | 72.66% ± 1.09 pp | 73.15% ± 0.64 pp | 1.82 ± 0.08 | 0.7259 ± 0.0166 | 0.7741 ± 0.0190 | 60,362 |

Seed-42 baseline difference from Exercise 2 (train/validation/test accuracy): +0.000000 / +0.000000 / +0.000000; matches tolerance: True.
Training time summed across all runs: 3946.6 s.

## Exercise 4 — Width and depth

Mean ± sample standard deviation over three seeds. Validation values are reported as percentages.

| Configuration | Parameters | MACs/image | Best-epoch validation accuracy | Final-epoch validation accuracy | Mean training time (s) |
|---|---:|---:|---:|---:|---:|
| Narrow CNN | 25,578 | 1,642,496 | 69.07% ± 0.31 pp | 67.84% ± 0.50 pp | 240.6 |
| Baseline-width CNN | 60,362 | 5,644,288 | 71.49% ± 0.24 pp | 68.69% ± 0.72 pp | 252.6 |
| Wide CNN | 157,578 | 20,725,760 | 72.85% ± 0.33 pp | 70.46% ± 0.38 pp | 271.4 |
| Shallow CNN | 21,386 | 905,216 | 67.27% ± 0.09 pp | 66.57% ± 0.70 pp | 258.3 |
| Medium CNN | 30,634 | 10,342,400 | 70.15% ± 0.34 pp | 69.35% ± 0.52 pp | 256.6 |
| Deep CNN | 39,882 | 19,779,584 | 70.75% ± 0.55 pp | 69.40% ± 0.20 pp | 257.5 |

The notebook loaded its 18 saved runs; no models were retrained.

## Figure files

- `artifacts/exercise_1/confusion_matrix.png`
- `artifacts/exercise_1/learning_curves.png`
- `artifacts/exercise_2/cnn_conv1_filters.png`
- `artifacts/exercise_2/cnn_validation_feature_maps.png`
- `artifacts/exercise_2/extra_pixel_shuffle/shuffle_examples.png`
- `artifacts/exercise_2/extra_pixel_shuffle/shuffled_loss_curves.png`
- `artifacts/exercise_2/extra_pixel_shuffle/test_accuracy_original_vs_shuffled.png`
- `artifacts/exercise_2/extra_pixel_shuffle/validation_accuracy_curves.png`
- `artifacts/exercise_2/learning_curves.png`
- `artifacts/exercise_2/mlp_cnn_class_recall.png`
- `artifacts/exercise_2/mlp_cnn_loss_comparison.png`
- `artifacts/exercise_2/mlp_cnn_parameters.png`
- `artifacts/exercise_2/mlp_cnn_test_accuracy.png`
- `artifacts/exercise_2/mlp_cnn_validation_accuracy.png`
- `artifacts/exercise_2/test_confusion_matrix.png`
- `artifacts/exercise_3/accuracy_comparison.png`
- `artifacts/exercise_3/accuracy_curves.png`
- `artifacts/exercise_3/augmentation_examples.png`
- `artifacts/exercise_3/learning_curves.png`
- `artifacts/exercise_3/train_test_gap.png`
- `artifacts/exercise_4/seed42_loss_curves_2x3.png`
- `artifacts/exercise_4/train_validation_accuracy_gap.png`
- `artifacts/exercise_4/validation_accuracy_by_depth.png`
- `artifacts/exercise_4/validation_accuracy_by_width.png`
- `artifacts/exercise_4/validation_accuracy_vs_macs.png`
- `artifacts/exercise_4/validation_accuracy_vs_parameters.png`
- `artifacts/exercise_4/width_depth_comparison.png`
