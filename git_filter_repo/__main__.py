import sys

from git_filter_repo import setup_gettext, FilteringOptions, RepoAnalyze, RepoFilter

def main():
  setup_gettext()
  args = FilteringOptions.parse_args(sys.argv[1:])
  if args.analyze:
    RepoAnalyze.run(args)
  else:
    filter = RepoFilter(args)
    filter.run()

if __name__ == '__main__':
  main()