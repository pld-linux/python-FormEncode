%define module FormEncode

Summary:	HTML form validation, generation, and convertion package
Summary(pl):	Modu³ do walidacji, tworzenia i konwersji formularzy HTML
Name:		python-%{module}
Version:	0.6
Release:	1
License:	PSF
Group:		Development/Languages/Python
Source0:	http://cheeseshop.python.org/packages/source/F/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	8504d515a8e25f1bba6842224b7494ae
URL:		http://formencode.org/
BuildRequires:	python
BuildRequires:	python-setuptools
%pyrequires_eq	python-modules
Requires:	python-elementtree
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FormEncode validates and converts nested structures. It allows for a
declarative form of defining the validation, and decoupled processes
for filling and generating forms.

%description -l pl
FormEncode s³u¿y do sprawdzania poprawno¶ci i konwersji zagnie¿d¿onych
struktur. Pozwala na deklaratywny sposób definiowania regu³ poprawno¶ci
i niezale¿ne od nich wype³nianie i generowanie formularzy.

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
%{py_sitescriptdir}/%{module}*
%{py_sitescriptdir}/*formencode*
%doc docs/*.txt
