Name: redborder-repo
Version: %{__version}
Release: %{__release}%{?dist}
BuildArch: noarch
Summary: package for redBorder repository	
BuildArch: noarch

Group: System Environment/Base
License: GPLv2
URL: https://github.com/redBorder/redborder-repo
Source0: %{name}-%{version}.tar.gz
Requires: epel-release

%description
This package contains the Extra Packages for redborder repository
as well as configuration for yum.

%prep
%setup -qn %{name}-%{version}

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg
install -D -m 644 resources/redborder.repo $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
install -D -m 644 resources/RPM-GPG-KEY-redborder-repo $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root)
/etc/yum.repos.d/redborder.repo
/etc/pki/rpm-gpg/RPM-GPG-KEY-redborder-repo

%changelog
* Mon Oct 31 2016 Juan J. Prieto <jjprieto@redborder.com> - 0.0.2-1
- Add gpg public key
* Fri Oct 28 2016 Juan J. Prieto <jjprieto@redborder.com> - 0.0.1-1
- first spec version

