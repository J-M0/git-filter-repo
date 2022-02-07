htmldir = $(datarootdir)/doc/git/html

TESTS = t/run_tests

dist_bin_SCRIPTS = git-filter-repo
dist_man1_MANS = Documentation/man1/git-filter-repo.1
dist_html_DATA = Documentation/html/git-filter-repo.html

CLEANFILES = $(dist_bin_SCRIPTS)

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

# People installing from tarball will already have man1/git-filter-repo.1 and
# html/git-filter-repo.html.  But let's support people installing from a git
# clone too; for them, just cheat and snag a copy of the built docs that I
# record in a different branch.
Documentation/man1/git-filter-repo.1:
	mkdir -p Documentation/man1
	git show origin/docs:man1/git-filter-repo.1 >Documentation/man1/git-filter-repo.1

Documentation/html/git-filter-repo.html:
	mkdir -p Documentation/html
	git show origin/docs:html/git-filter-repo.html >Documentation/html/git-filter-repo.html
