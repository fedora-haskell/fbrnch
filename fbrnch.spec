# generated by cabal-rpm-2.0.6 --standalone
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global gittag 3a2c1818b3f2a4d86dcd2cb94d044c19d9625680

%global ghc_without_dynamic 1
%global ghc_without_shared 1
%undefine with_ghc_prof
%undefine with_haddock
%global without_prof 1
%global without_haddock 1
%global debug_package %{nil}

Name:           fbrnch
Version:        0.1
Release:        10%{?dist}
Summary:        Build and create Fedora package repos and branches

License:        GPLv2+
Url:            https://github.com/juhp/fbrnch
# Begin cabal-rpm sources:
Source0:        https://github.com/juhp/fbrnch/archive/%{gittag}.tar.gz#/fbrnch-%{gittag}.tar.gz
# End cabal-rpm sources

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
Requires:       bodhi-client
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
install -D -t %{buildroot}%{_bindir} dist-newstyle/build/x86_64-linux/ghc-8.6.5/fbrnch-0.1/x/fbrnch/build/fbrnch/fbrnch


%files
# Begin cabal-rpm files:
%license LICENSE
%doc CHANGELOG.md README.md TODO
%{_bindir}/%{name}
# End cabal-rpm files


%changelog
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
