%define module FormEncode

Summary:	HTML form validation, generation, and convertion package
Summary(pl.UTF-8):	Moduł do walidacji, tworzenia i konwersji formularzy HTML
Name:		python-%{module}
Version:	1.2.2
Release:	1
License:	PSF
Group:		Development/Languages/Python
Source0:	http://cheeseshop.python.org/packages/source/F/FormEncode/%{module}-%{version}.tar.gz
# Source0-md5:	da23d54af521d1feab12b4caf30e3111
URL:		http://formencode.org/
BuildRequires:	python >= 1:2.4
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FormEncode validates and converts nested structures. It allows for a
declarative form of defining the validation, and decoupled processes
for filling and generating forms.

%description -l pl.UTF-8
FormEncode służy do sprawdzania poprawności i konwersji zagnieżdżonych
struktur. Pozwala na deklaratywny sposób definiowania reguł poprawności
i niezależne od nich wypełnianie i generowanie formularzy.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python ./setup.py install \
        --single-version-externally-managed \
        --optimize=2 \
        --root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*.txt
%{py_sitescriptdir}/%{module}*
%{py_sitescriptdir}/*formencode*
