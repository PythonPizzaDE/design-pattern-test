from abc import abstractmethod, ABC

class InstallerStrategie(ABC):
    @abstractmethod
    def install(self, pkg: str) -> None:
        pass

class PacmanStrategie(InstallerStrategie):
    def install(self, pkg: str) -> None:
        print(f'installing {pkg} with pacman' )

class DNFStrategie(InstallerStrategie):
    def install(self, pkg: str) -> None:
        print(f'installing {pkg} with dnf' )

class Installer:
    def __init__(self, strategie: InstallerStrategie) -> None:
        self.strategie = strategie

    def install(self, pkg: str) -> None:
        self.strategie.install(pkg)

arch_installer = Installer(PacmanStrategie())
fedora_installer = Installer(DNFStrategie())

fedora_installer.install('neovim')
arch_installer.install('neovim')
arch_installer.install('paulfrische')
