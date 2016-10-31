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
mkdir -p $RPM_BUILD_ROOT/etc/yum.repos.d
install -D -m 644 resources/redborder.repo $RPM_BUILD_ROOT/etc/yum.repos.d/

%files
%defattr(0644,root,root)
/etc/yum.repos.d/redborder.repo

%changelog
* Fri Oct 28 2016 Juan J. Prieto <jjprieto@redborder.com> - 0.0.1-1
- first spec version

