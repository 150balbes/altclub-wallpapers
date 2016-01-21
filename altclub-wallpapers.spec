Name:		altclub-wallpapers
Version:	0.0.1
Release:	alt1
Summary:	AltLinux Club Users Wallpapers

License:	GPL
Group:		Graphical desktop/Icewm
URL:		https://github.com/150balbes/altclub-wallpapers
Packager:	Oleg Ivanov <Leo-sp150@yandex.ru>

Source0:	wallpapers.tar.bz2

%description
AltLinux Club Users Wallpapers

%prep

%build
%make_build

%install
mkdir -p %buildroot%_datadir/wallpapers
tar xjf %SOURCE0 -C %buildroot%_datadir/

%files
%_datadir/*

%changelog
* Tue Jan 19 2016 Oleg Ivanov <Leo-sp150@yandex.ru> 0.0.1-alt2
- init ver
