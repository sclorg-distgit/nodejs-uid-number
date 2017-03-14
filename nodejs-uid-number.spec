%{?scl:%scl_package nodejs-uid-number}
%{!?scl:%global pkg_name %{name}}
%global enable_tests 0
%{?nodejs_find_provides_and_requires}

Name:       %{?scl_prefix}nodejs-uid-number
Version:    0.0.6
Release:    1%{?dist}
Summary:    Convert a username/group name to a UID/GID number
License:    ISC
URL:        https://github.com/isaacs/uid-number
Source0:    http://registry.npmjs.org/uid-number/-/uid-number-%{version}.tgz
BuildArch:  noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{enable_tests}
BuildRequires:    %{?scl_prefix}npm(
%endif

%description
%{summary}.

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/uid-number
cp -pr *.js package.json %{buildroot}%{nodejs_sitelib}/uid-number

chmod 0644 %{buildroot}%{nodejs_sitelib}/uid-number/get-uid-gid.js

%nodejs_symlink_deps

%if 0%{enable_tests}
%check
%nodejs_symlink_deps --check

%endif

%files
%{nodejs_sitelib}/uid-number
%doc README.md LICENSE

%changelog
* Wed Sep 07 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.0.6-1
- Updated with script

* Thu Jun 09 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.0.5-3
- Resolves: rhbz#1334856 , fixes wrong license

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.0.5-2
- rebuilt

* Mon Jan 12 2015 Tomas Hrcka <thrcka@redhat.com> - 0.0.5-1
- New upstream release 0.0.5

* Thu Oct 17 2013 Tomas Hrcka <thrcka@redhat.com> - 0.0.3-7
- replace provides and requires with macro

* Thu Apr 11 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.0.3-6
- Add support for software collections

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 11 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.3-4
- really use a fresh tarball from upstream
- fix permissions
- include LICENCE file

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.3-3
- add missing build section
- rebuild with fresh tarball from upstream

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.3-2
- Clean up for submission

* Wed Mar 28 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.3-1
- initial package
