%global tl_name pgfopts
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1a
Release:	%{tl_revision}.1
Summary:	LaTeX package options with pgfkeys
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pgfopts
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfopts.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfopts.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfopts.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(pgf)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The pgfkeys package (part of the pgf distribution) is a well-designed
way of defining and using large numbers of keys for key-value syntaxes.
However, pgfkeys itself does not offer means of handling LaTeX class and
package options. This package adds such option handling to pgfkeys, in
the same way that kvoptions adds the same facility to the LaTeX standard
keyval package.

