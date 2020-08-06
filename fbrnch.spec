# generated by cabal-rpm-2.0.6 --standalone
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global gittag 5a44f81e8990a6a90e4b2729191b4f8d4dee912b

%global ghc_without_dynamic 1
%global ghc_without_shared 1
%undefine with_ghc_prof
%undefine with_haddock
%global without_prof 1
%global without_haddock 1
%global debug_package %{nil}

Name:           fbrnch
Version:        0.3
Release:        2%{?dist}
Summary:        Build and create Fedora package repos and branches

License:        GPLv2+
Url:            https://github.com/juhp/fbrnch
# Begin cabal-rpm sources:
Source0:        https://github.com/juhp/fbrnch/archive/%{gittag}.tar.gz#/fbrnch-%{gittag}.tar.gz
# End cabal-rpm sources
# made with `fbrnch --bash-completion-script fbrnch | sed s/filenames/default/`:
Source1:        bash_completion

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-base-devel
#BuildRequires:  ghc-bodhi-devel
#BuildRequires:  ghc-bugzilla-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-config-ini-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-email-validate-devel
BuildRequires:  ghc-extra-devel
#BuildRequires:  ghc-fedora-dists-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-http-conduit-devel
BuildRequires:  ghc-http-directory-devel
#BuildRequires:  ghc-koji-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-optparse-applicative-devel
#BuildRequires:  ghc-pagure-devel
#BuildRequires:  ghc-rpmbuild-order-devel
BuildRequires:  ghc-simple-cmd-devel
BuildRequires:  ghc-simple-cmd-args-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-xdg-basedir-devel
BuildRequires:  cabal-install > 2
# End cabal-rpm deps
# for missing deps:
BuildRequires:  ghc-base64-bytestring-devel
BuildRequires:  ghc-fgl-devel
BuildRequires:  ghc-io-streams-devel
BuildRequires:  ghc-iso8601-time-devel
BuildRequires:  ghc-lens-aeson-devel
BuildRequires:  ghc-old-time-devel
BuildRequires:  ghc-polyparse-devel
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  ghc-zlib-bindings-devel
# for cabal.project repos
BuildRequires:  git-core
# for HsOpenSSL
BuildRequires:  openssl-devel
# manpage
BuildRequires:  help2man
Requires:       bodhi-client
Requires:       copr-cli
Requires:       curl
Requires:       fedpkg
Requires:       git-core
Requires:       koji
Requires:       krb5-workstation
Requires:       openssh-clients
Requires:       rpm-build
Requires:       rpmdevtools

%description
Fed Brnch is a convenient packaging tool for Fedora Packagers, with integration
for bugzilla, koji, and bodhi.

Features include:
- create and update package reviews and list them
- create repo and branch requests for new approved packages
- import srpms from package reviews
- merge between Fedora branches and build them
- package status command.


%prep
%setup -q -n %{name}-%{gittag}


%build
%global cabal cabal
%cabal v2-update
%cabal v2-build


%install
%define binfile dist-newstyle/build/%{_arch}-linux/ghc-*/%{name}-%{version}/x/fbrnch/build/fbrnch/fbrnch
install -D -t %{buildroot}%{_bindir} %{binfile}

install -pm 644 -D %{SOURCE1} %{buildroot}%{_datadir}/bash-completion/completions/%{name}

help2man --no-info %{binfile} > %{name}.man
install -pm 644 -D %{name}.man %{buildroot}%{_mandir}/man1/%{name}.1


%files
# Begin cabal-rpm files:
%license LICENSE
%doc CHANGELOG.md README.md TODO
%{_bindir}/%{name}
# End cabal-rpm files
%{_datadir}/bash-completion/completions/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Fri Aug  7 2020 Jens Petersen <petersen@redhat.com> - 0.3-2 (5a44f81)
- revert back from using "." for rpmbuild macros dir options

* Thu Aug  6 2020 Jens Petersen <petersen@redhat.com> - 0.3-1 (acb05de)
- install: don't build if existing rpm files newer than spec
  and add --rebuild and --short-circuit options
- use absolute paths for sudo and dnf everywhere
- add 'copr' build command (ported from juhp/cobrnch)

* Wed Aug  5 2020 Jens Petersen <petersen@redhat.com> - 0.2-9 (7499a63)
- improve mock results dir paths like fedpkg

* Wed Aug  5 2020 Jens Petersen <petersen@redhat.com> - 0.2-8 (9462af2)
- support .git file repos also for prepping and building

* Wed Aug  5 2020 Jens Petersen <petersen@redhat.com> - 0.2-7 (d65baee)
- fix srpm generation when _sourcedir is user undefined

* Tue Aug  4 2020 Jens Petersen <petersen@redhat.com> - 0.2-6 (70e945c)
- local: print uninstalled deps
- sort: --with/--without options (rpmbuild-order-0.4.2) (#5)
- support absorbed git submodules (#8)
- build: experimental --dry-run option
- build: Bodhi --update-type option (#7)

* Tue Aug  4 2020 Jens Petersen <petersen@redhat.com> - 0.2-5 (4784a63)
- build now does git fetch and merge of origin
- clone: output package names to show progress
- wait-repo's now show datestamp
- build: maybe override and waitrepo when build already complete
- sort/parallel: update to rpmbuild-order-0.4.1 which also shows any subcycles

* Wed Jul 29 2020 Jens Petersen <petersen@redhat.com> - 0.2-4 (f7a009d)
- parallel: only override when no target or not stable
- parallel: fixed to switch to branch
- update to rpmbuild-0.4.0 release with bugfixes:
  (Provide Name and parse package name dirs with a dot)

* Wed Jul 29 2020 Jens Petersen <petersen@redhat.com> - 0.2-3 (570d531)
- parallel: do override for built package if not tagged (#3)
  - reported by QuLogic
- fix pull command and check for clean working dir
- latest rpmbuild-order fixes a recent regression
- be more lenient when package is in a old branch
- generate a basic manpage with help2man

* Thu Jul 23 2020 Jens Petersen <petersen@redhat.com> - 0.2-2 (9b8982d)
- further simply the option/arg parsing for better error messages

* Wed Jul 22 2020 Jens Petersen <petersen@redhat.com> - 0.2-1 (d8c9a66)
- build/merge/status by default now only act on the current branch
  and require a branch option when more than one package
- use -B or --all-branches to act on all branches like before
- read Koji for correct buildtag for wait-repo
- ignore sources file when not dist-git

* Wed Jul 22 2020 Jens Petersen <petersen@redhat.com> - 0.1-12
- bash completions

* Tue Jul 21 2020 Jens Petersen <petersen@redhat.com> - 0.1-11 (5d9e3af)
- mock: add --root option (takes a branch)

* Tue Jul 21 2020 Jens Petersen <petersen@redhat.com> - 0.1-10 (3a2c181)
- build/parallel: check no existing koji task which is not yet building
- parallel: rpmbuild-order now preserves dir paths to packages
- scratch: allow multiple --arch options

* Sun Jul 19 2020 Jens Petersen <petersen@redhat.com> - 0.1-9 (8492abd)
- 'build' now does wait-repo between packages
- 'build' always checks sources file up to date
- 'build' can now rejoin started builds
- new 'parallel' build command for building packages in dependency layers
- new 'diff' command for checking changes across many packages
- new 'commit' command for committing changes across many packages
- prep now prints nvr
- 'install' handles reinstalls correctly (when only some subpackages installed)
- ignore remote branches other than origin

* Wed Jul 15 2020 Jens Petersen <petersen@redhat.com> - 0.1-8 (e5dd3f3)
- local --short-circuit
- interleaved output for prep and local errors

* Fri Jul 10 2020 Jens Petersen <petersen@redhat.com> - 0.1-7 (981285c)
- build: allow pushing/building before current HEAD
- scratch: add --rebuild-srpm option (default is --no-rebuild-srpm)
- status: allow dirty working dir

* Sat Jul  4 2020 Jens Petersen <petersen@redhat.com> - 0.1-6 (254130a)
- scratch: --arch option and don't get sources too early
- build: drop --scratch
- srpm and mock commands

* Fri Jul  3 2020 Jens Petersen <petersen@redhat.com> - 0.1-5 (7d0e70d)
- 'scratch' build command
- 'build' options --override and --no-fail-fast

* Thu Jul  2 2020 Jens Petersen <petersen@redhat.com> - 0.1-4 (cdeaffb)
- create-review/updatereview: now run rpmlint and optionally mock

* Thu Jul  2 2020 Jens Petersen <petersen@redhat.com> - 0.1-3 (6fd8b0a)
- local, install: install deps

* Wed Jul  1 2020 Jens Petersen <petersen@redhat.com> - 0.1-2 (4612be2)
- prep, local, install: pull down sources now
- add Requires for client tools

* Wed Jul  1 2020 Jens Petersen <petersen@redhat.com> - 0.1-1 (4fe8239)
- initial package
