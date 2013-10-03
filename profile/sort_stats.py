import pstats

stats = pstats.Stats("stats.out")
stats.strip_dirs().sort_stats("cumulative").print_stats()
