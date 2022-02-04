htmldir = $(datarootdir)/doc/git/html

TESTS = t/run_tests

dist_bin_SCRIPTS = git-filter-repo
dist_man1_MANS = Documentation/man1/git-filter-repo.1
dist_html_DATA = Documentation/html/git-filter-repo.html

EXTRA_DIST = t

clean-local:
	rm -rf t/trash*

.PHONY: coverage
coverage:
	time t/run_coverage

# fixup_locale might matter once we actually have translations, but right now
# we don't.  It might not even matter then, because python has a fallback podir.
.PHONY: fixup_locale
fixup_locale:
	sed -i -e 's%@@LOCALEDIR@@%$(localedir)%' git-filter-repo

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

# Fixup the shebang for installation
install-exec-hook:
	printf '1,s|#!/usr/bin/env python3|#!$(PYTHON)|\nwq\n' | ed $(DESTDIR)/$(bindir)/git-filter-repo
