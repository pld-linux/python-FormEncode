#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define	module	FormEncode
Summary:	HTML form validation, generation, and convertion package
Summary(pl.UTF-8):	Moduł do walidacji, tworzenia i konwersji formularzy HTML
Name:		python-%{module}
# keep 2.0.x here for python2 support
Version:	2.0.1
Release:	1
License:	PSF
Group:		Development/Languages/Python
#Source0Download: https://pypi.org/project/FormEncode/
Source0:	https://files.pythonhosted.org/packages/source/F/FormEncode/%{module}-%{version}.tar.gz
# Source0-md5:	65a9ba7220890c3d26904bdafe3a5a35
URL:		http://formencode.org/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm < 6
BuildRequires:	python-setuptools_scm_git_archive
%if %{with tests}
BuildRequires:	python-dns = 1.16.0
BuildRequires:	python-pycountry < 19
BuildRequires:	python-pytest < 4.7
BuildRequires:	python-six
%endif
%endif
%if %{with python3}
BuildRequires:	python3-2to3 >= 1:3.6
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
BuildRequires:	python3-setuptools_scm_git_archive
%if %{with tests}
BuildRequires:	python3-dns >= 2.0.0
BuildRequires:	python3-pycountry >= 16.10.23
BuildRequires:	python3-pytest
BuildRequires:	python3-six
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FormEncode validates and converts nested structures. It allows for a
declarative form of defining the validation, and decoupled processes
for filling and generating forms.

%description -l pl.UTF-8
FormEncode służy do sprawdzania poprawności i konwersji zagnieżdżonych
struktur. Pozwala na deklaratywny sposób definiowania reguł
poprawności i niezależne od nich wypełnianie i generowanie formularzy.

%package -n python3-%{module}
Summary:	HTML form validation, generation, and convertion package
Summary(pl.UTF-8):	Moduł do walidacji, tworzenia i konwersji formularzy HTML
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.6

%description -n python3-%{module}
FormEncode validates and converts nested structures. It allows for a
declarative form of defining the validation, and decoupled processes
for filling and generating forms.

%description -n python3-%{module} -l pl.UTF-8
FormEncode służy do sprawdzania poprawności i konwersji zagnieżdżonych
struktur. Pozwala na deklaratywny sposób definiowania reguł
poprawności i niezależne od nich wypełnianie i generowanie formularzy.

%package apidocs
Summary:	API documentation for Python FormEncode module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona FormEncode
Group:		Documentation

%description apidocs
API documentation for Python FormEncode module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona FormEncode.

%prep
%setup -q -n %{module}-%{version}

# uses network to validate domains (with one no longer valid anyway)
%{__rm} formencode/tests/test_email.py
# validator doctests cover Email and URL validators which include DNS lookups
%{__sed} -i -e '/^modules / s/, validators//' formencode/tests/test_doctests.py

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m pytest build-2/lib/formencode/tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m pytest build-3/lib/formencode/tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%{__mv} $RPM_BUILD_ROOT%{py_sitescriptdir}/docs built-docs

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/formencode/tests
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/formencode/i18n/FormEncode.pot
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/formencode/i18n/*/LC_MESSAGES/FormEncode.po
%py_postclean

find $RPM_BUILD_ROOT%{py_sitescriptdir}/formencode/i18n -type d -maxdepth 1 | \
	%{__sed} -ne "s,$RPM_BUILD_ROOT\(.*i18n/\([a-z]\+\(_[A-Z][A-Z]\)\?\).*\),%%lang(\2) \1,p" > py2.lang
%endif

%if %{with python3}
%py3_install

%{__rm} -rf built-docs
%{__mv} $RPM_BUILD_ROOT%{py3_sitescriptdir}/docs built-docs

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/formencode/tests
%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/formencode/i18n/FormEncode.pot
%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/formencode/i18n/*/LC_MESSAGES/FormEncode.po

find $RPM_BUILD_ROOT%{py3_sitescriptdir}/formencode/i18n -type d -maxdepth 1 | \
	%{__sed} -ne "s,$RPM_BUILD_ROOT\(.*i18n/\([a-z]\+\(_[A-Z][A-Z]\)\?\).*\),%%lang(\2) \1,p" > py3.lang
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files -f py2.lang
%defattr(644,root,root,755)
%doc README.rst
%dir %{py_sitescriptdir}/formencode
%{py_sitescriptdir}/formencode/*.py[co]
%dir %{py_sitescriptdir}/formencode/i18n
%{py_sitescriptdir}/formencode/javascript
%{py_sitescriptdir}/FormEncode-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module} -f py3.lang
%defattr(644,root,root,755)
%doc README.rst
%dir %{py3_sitescriptdir}/formencode
%{py3_sitescriptdir}/formencode/*.py
%{py3_sitescriptdir}/formencode/__pycache__
%dir %{py3_sitescriptdir}/formencode/i18n
%{py3_sitescriptdir}/formencode/javascript
%{py3_sitescriptdir}/FormEncode-%{version}-py*.egg-info
%endif

%files apidocs
%defattr(644,root,root,755)
%doc built-docs/*
