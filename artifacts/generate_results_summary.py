from pathlib import Path
import json
import pandas as pd

ROOT = Path.cwd()
A = ROOT / "artifacts"
ex1 = json.loads((A / "exercise_1" / "results.json").read_text(encoding="utf-8"))
ex2 = json.loads((A / "exercise_2" / "results.json").read_text(encoding="utf-8"))
shuffle = json.loads((A / "exercise_2" / "extra_pixel_shuffle" / "results.json").read_text(encoding="utf-8"))
ex3 = json.loads((A / "exercise_3" / "results.json").read_text(encoding="utf-8"))
ex4 = json.loads((A / "exercise_4" / "experiment_results.json").read_text(encoding="utf-8"))
comparison = pd.read_csv(A / "exercise_2" / "mlp_cnn_comparison.csv")

def pct(v): return f"{100*float(v):.2f}%"
def val(v): return f"{float(v):.4f}"
def loss(v): return f"{float(v):.4f}"

lines = ["# CIFAR-10 Assessment: Results Summary", "", "Generated from the saved exercise result files.", ""]

m = ex1["final_metrics"]
b = ex1["best_validation_loss"]
lines += ["## Exercise 1 — MLP", "", "| Checkpoint | Train accuracy | Validation accuracy | Test accuracy | Train loss | Validation loss | Test loss | Parameters |", "|---|---:|---:|---:|---:|---:|---:|---:|"]
lines.append(f"| Final epoch | {pct(m['train']['accuracy'])} | {pct(m['validation']['accuracy'])} | {pct(m['test']['accuracy'])} | {loss(m['train']['loss'])} | {loss(m['validation']['loss'])} | {loss(m['test']['loss'])} | {ex1['trainable_parameters']:,} |")
lines.append(f"| Best validation-loss checkpoint (epoch {b['epoch']}) | {pct(b['train']['accuracy'])} | {pct(b['validation']['accuracy'])} | {pct(b['test']['accuracy'])} | {loss(b['train']['loss'])} | {loss(b['validation']['loss'])} | {loss(b['test']['loss'])} | {ex1['trainable_parameters']:,} |")
lines += ["", f"Training time: {ex1['training_seconds']:.1f} s. Validation-loss minimum: epoch {b['epoch']}, {loss(b['best_validation_loss'])}.", ""]

lines += ["## Exercise 2 — CNN baseline and comparisons", "", "| Model/checkpoint | Train accuracy | Validation accuracy | Test accuracy | Train loss | Validation loss | Test loss | Train–test gap (pp) | Parameters |", "|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
for _,r in comparison.iterrows():
 lines.append(f"| {r['model']} — {r['checkpoint']} | {pct(r['train_accuracy'])} | {pct(r['validation_accuracy'])} | {pct(r['test_accuracy'])} | {loss(r['train_loss'])} | {loss(r['validation_loss'])} | {loss(r['test_loss'])} | {float(r['train_test_accuracy_gap_pp']):.2f} | {int(r['trainable_parameters']):,} |")
mlp_final = float(comparison[(comparison.model=='MLP') & (comparison.checkpoint=='Final epoch')].iloc[0].test_accuracy)
cnn_final = float(comparison[(comparison.model=='CNN') & (comparison.checkpoint=='Final epoch')].iloc[0].test_accuracy)
mlp_early = float(comparison[(comparison.model=='MLP') & (comparison.checkpoint=='Best validation-loss checkpoint')].iloc[0].test_accuracy)
cnn_early = float(comparison[(comparison.model=='CNN') & (comparison.checkpoint=='Best validation-loss checkpoint')].iloc[0].test_accuracy)
lines += ["", f"CNN minus MLP test accuracy: {100*(cnn_final-mlp_final):+.2f} pp at the final epoch; {100*(cnn_early-mlp_early):+.2f} pp for the best-validation-loss checkpoints.", f"Final CNN training time: {ex2['training_seconds']:.1f} s. CNN validation-loss checkpoint: epoch {ex2['best_validation_loss']['epoch']}.", "", "### Pixel-shuffle investigation", "", "| Model | Original test accuracy | Shuffled-pixel test accuracy | Change (pp) |", "|---|---:|---:|---:|"]
for model in ["MLP", "CNN"]:
 orig=shuffle['metrics'][f'{model} original']['test']['accuracy']
 shuf=shuffle['metrics'][f'{model} shuffled']['test']['accuracy']
 lines.append(f"| {model} | {pct(orig)} | {pct(shuf)} | {100*(shuf-orig):+.2f} |")
lines.append("")

lines += ["## Exercise 3 — Regularisation", "", "Mean ± sample standard deviation over the three seeds.", "", "| Condition | Train accuracy | Validation accuracy | Test accuracy | Train–test gap (pp) | Train loss | Test loss | Parameters |", "|---|---:|---:|---:|---:|---:|---:|---:|"]
for r in ex3['aggregated']:
 lines.append(f"| {r['condition']} | {pct(r['train_accuracy_mean'])} ± {100*r['train_accuracy_std']:.2f} pp | {pct(r['validation_accuracy_mean'])} ± {100*r['validation_accuracy_std']:.2f} pp | {pct(r['test_accuracy_mean'])} ± {100*r['test_accuracy_std']:.2f} pp | {r['train_test_gap_pp_mean']:.2f} ± {r['train_test_gap_pp_std']:.2f} | {loss(r['train_loss_mean'])} ± {r['train_loss_std']:.4f} | {loss(r['test_loss_mean'])} ± {r['test_loss_std']:.4f} | {r['parameters']:,} |")
diff=ex3['baseline_cross_check']['differences']
lines += ["", f"Seed-42 baseline difference from Exercise 2 (train/validation/test accuracy): {diff['train_accuracy']:+.6f} / {diff['validation_accuracy']:+.6f} / {diff['test_accuracy']:+.6f}; matches tolerance: {ex3['baseline_cross_check']['matches_to_0.0001']}.", f"Training time summed across all runs: {sum(float(r['training_seconds']) for r in ex3['runs']):.1f} s.", ""]

lines += ["## Exercise 4 — Width and depth", "", "Mean ± sample standard deviation over three seeds. Validation values are reported as percentages.", "", "| Configuration | Parameters | MACs/image | Best-epoch validation accuracy | Final-epoch validation accuracy | Mean training time (s) |", "|---|---:|---:|---:|---:|---:|"]
for r in ex4['aggregated']:
 lines.append(f"| {r['display_name']} | {r['trainable_parameters_mean']:,.0f} | {r['macs_per_image_mean']:,.0f} | {100*r['best_validation_accuracy_mean']:.2f}% ± {100*r['best_validation_accuracy_std']:.2f} pp | {100*r['final_validation_accuracy_mean']:.2f}% ± {100*r['final_validation_accuracy_std']:.2f} pp | {r['training_seconds_mean']:.1f} |")
lines += ["", "The notebook loaded its 18 saved runs; no models were retrained.", "", "## Figure files", ""]
for exercise in range(1,5):
 folder=A/f"exercise_{exercise}"
 for p in sorted(folder.rglob('*.png')):
  if 'cpu_run_archive' in p.parts: continue
  lines.append(f"- `{p.relative_to(ROOT).as_posix()}`")
lines.append("")
(A/"results_summary.md").write_text("\n".join(lines),encoding="utf-8")
print('Generated',A/'results_summary.md')
