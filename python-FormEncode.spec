%define module FormEncode
%define _module formencode

Summary:	HTML form validation, generation, and convertion package
Summary(pl):	Modu³ do walidacji, tworzenia i konwersji formularzy HTML
Name:		python-%{module}
Version:	0.3
Release:	1
License:	PSF
Group:		Development/Languages/Python
Source0:	http://cheeseshop.python.org/packages/source/F/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	57afa5aad26bf3acb8b00e4babfe8297
Patch0:		%{name}-disable-setuptools.patch
URL:		http://formencode.org/
BuildRequires:	python
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
%patch0 -p1

%build
rm -rf ez_setup
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir}/%{_module}/ -name \*.py | xargs rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/%{_module}
%doc docs/*.txt
