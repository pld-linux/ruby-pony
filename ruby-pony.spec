#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	pony
Summary:	The express way to send mail from Ruby
Name:		ruby-%{pkgname}
Version:	1.5.1
Release:	2
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	8a3627564e2254c0bcae29eb536ad778
URL:		http://github.com/benprew/pony
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-rspec >= 2.0.0
%endif
Requires:	ruby-mail >= 2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Send email in one command.

%prep
%setup -q -n %{pkgname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rdoc
%{ruby_vendorlibdir}/%{pkgname}.rb
