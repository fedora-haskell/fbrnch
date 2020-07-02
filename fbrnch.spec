# generated by cabal-rpm-2.0.6 --standalone
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global gittag 6fd8b0ac7dd3a4911139ad319eae26fcbf50e070

%global ghc_without_dynamic 1
%global ghc_without_shared 1
%undefine with_ghc_prof
%undefine with_haddock
%global without_prof 1
%global without_haddock 1
%global debug_package %{nil}

Name:           fbrnch
Version:        0.1
Release:        3%{?dist}
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
for bugzilla, koji, and bodhi. Features include: - create and update package
reviews and list them - create repo and branch requests for new approved
packages - import srpms from package reviews - merge between Fedora branches
and build them - package status command.


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
* Thu Jul  2 2020 Jens Petersen <petersen@redhat.com> - 0.1-3.git6fd8b0a
- local, install: install deps

* Thu Jul  2 2020 Jens Petersen <petersen@redhat.com> - 0.1-2.git4612be2
- prep, local, install: pull down sources now
- add Requires for client tools

* Wed Jul  1 2020 Jens Petersen <petersen@redhat.com> - 0.1-1.git4fe8239
- initial package
