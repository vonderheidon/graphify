# #0013 Full regression gate exposed nondeterministic completion ordering in test_label_communities_batches_when_over_batch_size: calls were [100, 50, 100] instead of submission order [100, 100, 50].

- 2026-06-30T20:53:20Z `issue`: Full regression gate exposed nondeterministic completion ordering in test_label_communities_batches_when_over_batch_size: calls were [100, 50, 100] instead of submission order [100, 100, 50]. [tests/test_labeling.py:278]
- 2026-06-30T20:53:20Z `attempt`: Post-rollout-fix full suite reached 2547 passes and 3 skips but failed the unrelated concurrent batching order assertion once. [tests/test_labeling.py:278] (failed)
- 2026-06-30T20:55:09Z `attempt`: The concurrent batching test passed isolated and the repeated full suite passed 2548 tests with 3 skips, confirming the earlier ordering assertion was flaky. [tests/test_labeling.py:278] (worked)
- 2026-06-30T20:55:09Z `fix`: No product change required for the one-off concurrent completion-order fluctuation; isolated and full reruns are green. [tests/test_labeling.py:278]
