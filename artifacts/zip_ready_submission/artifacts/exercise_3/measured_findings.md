# Exercise 3: measured findings

### Results and interpretation

The baseline was retrained in Exercise 3 on the GPU using the shared settings. Its seed-42 train, validation, and test accuracies match the Exercise 2 final-epoch baseline to 0.0001. Actual differences (Exercise 3 minus Exercise 2) were +0.000000 for training, +0.000000 for validation, and +0.000000 for test accuracy. The mean final-epoch baseline test accuracy across seeds was 68.81%.

- **Dropout:** test accuracy changed by +4.94 pp ? 1.26 pp versus the retrained baseline; the train-to-test gap changed by -13.00 pp ? 0.57 pp.
- **Augmentation:** test accuracy changed by +5.83 pp ? 1.13 pp versus the retrained baseline; the train-to-test gap changed by -20.41 pp ? 0.76 pp.
- **Dropout + Augmentation (additional combined run):** test accuracy changed by +4.34 pp ? 0.98 pp versus the retrained baseline; the train-to-test gap changed by -21.24 pp ? 0.56 pp.

Dropout and augmentation test-accuracy means differed by 0.89 pp, which does not exceed their combined seed standard deviation of 1.26 pp. With three seeds this is a heuristic, not a significance test. The seed standard deviations do not include variation from a different train/validation split.

The additional combined run reached mean test accuracy 73.15% and a mean train-to-test gap of 1.82 pp. It is reported separately and is not used to replace the primary single-intervention comparisons.

The Exercise 2 early-stopped CNN is a separate validation-loss-selected reference from epoch 7 with test accuracy 71.43%, compared with 68.50% for the Exercise 2 final-epoch CNN. Part of this difference is consistent with avoiding later overfitting in the 20-epoch baseline; the early-stopped result is not part of the controlled Exercise 3 comparison.

Dropout can reduce co-adaptation by preventing the output layer from relying too heavily on particular flattened features. Random crops and flips expose the CNN to translated and mirrored training views, encouraging some tolerance to those changes. This experiment treats crop and flip as one pipeline.

Limitations include three seeds, one fixed split, one dropout probability, crop and flip evaluated together, no weight decay, and a 20-epoch budget. Test accuracy is descriptive and did not guide condition selection.
