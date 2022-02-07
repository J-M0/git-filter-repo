htmldir = $(datarootdir)/doc/git/html

TESTS = t/run_tests

dist_bin_SCRIPTS = git-filter-repo
dist_man1_MANS = Documentation/git-filter-repo.1
dist_html_DATA = Documentation/git-filter-repo.html

CLEANFILES = $(dist_bin_SCRIPTS) $(dist_man1_MANS) $(dist_html_DATA)

EXTRA_DIST = t

git-filter-repo: git-filter-repo.in
	sed -e 's,[@]PYTHON[@],$(PYTHON),g' \
	    -e 's,[@]LOCALEDIR[@],$(localedir),g' \
		< git-filter-repo.in > git-filter-repo
	chmod +x git-filter-repo

clean-local:
	rm -rf t/trash*

.PHONY: coverage
coverage:
	time t/run_coverage

Documentation/git-filter-repo.1 Documentation/git-filter-repo.html: Documentation/git-filter-repo.txt
	test -d ../git
	ln -sf ../../git-filter-repo/Documentation/git-filter-repo.txt ../git/Documentation/
	$(MAKE) -C ../git/Documentation git-filter-repo.html git-filter-repo.1
	cp -a ../git/Documentation/git-filter-repo.html Documentation/
	cp -a ../git/Documentation/git-filter-repo.1 Documentation/
