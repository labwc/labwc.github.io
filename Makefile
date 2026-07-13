# When doing local development on .md files, just run make to build the files
# that changed rather than all.
#
# If src/template_* files are changed, all files need to be re-built

all:
	@ONLY_BUILD_FILES_THAT_CHANGED=t ./build-site
