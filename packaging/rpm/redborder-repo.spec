Name: redborder-repo
Version: %{__version}
Release: %{__release}%{?dist}
BuildArch: noarch
Summary: package for redBorder repository

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
sed -i "s/{{PRODUCT_VERSION}}/$__product_version/g" resources/redborder.repo
sed -i "s/{{REPO_URL}}/$__repo_url/g" resources/redborder.repo

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
* Frid Sep 22 2023 Miguel Negrón <manegron@redborder.com> - 1.0.0-1
- Move to rhel9
* Wed Jan 27 2020 Juan J. Prieto <jjprieto@redborder.com> - 0.0.5-1
- Replace logstash 6 repo by 7
* Thu Jan 24 2018 Juan J. Prieto <jjprieto@redborder.com> - 0.0.4-1
- Add logstash repo
* Thu Nov 03 2016 Juan J. Prieto <jjprieto@redborder.com> - 0.0.3-1
- Fix host mapping
* Mon Oct 31 2016 Juan J. Prieto <jjprieto@redborder.com> - 0.0.2-1
- Add gpg public key
* Fri Oct 28 2016 Juan J. Prieto <jjprieto@redborder.com> - 0.0.1-1
- first spec version

