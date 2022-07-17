import os
import pytest
import shutil

PREFETCH = os.path.join(os.environ.get("WINDIR"), "Prefetch")
TEMP = os.path.join(os.environ.get("WINDIR"), "TEMP")
USER_TEMP = os.environ.get("TEMP")

class TestCleanUp:
    
    def get_contents(self, path):
        return (os.path.join(path, item) for item in os.listdir(path))
        
    @pytest.mark.parametrize('path', (PREFETCH, TEMP, USER_TEMP))
    def test_delete(self, path):
        print("\n")
        
        for item in self.get_contents(path):
            
            try:
                if os.path.isfile(item):
                    print(f"Deleting File {item}")
                    os.remove(item)
                else:
                    print(f"Deleting Directory {item}")
                    shutil.rmtree(item)
            except PermissionError as e:
                if "Access is denied" in str(e):
                    print(f"Could not delete {item} due to Permission Error")
     
    @pytest.mark.parametrize('image', ('SearchApp.exe', 'WinStore.App.exe', 'RuntimeBroker.exe', 'TextInputHost.exe', 'SearchApp.exe', 'IntelCpHDCPSvc.exe'))
    def test_stop_process(self, image):
        print("\n")
        
        try:
            print(f"Stopping Process {image}")
            os.system(f"taskkill /F /im {image}")
        except:
            pytest.skip(f"Cannot Stop Process {image}")
        
        