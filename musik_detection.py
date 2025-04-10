import soundcard as sc
import numpy as np
import time
import os
from collections import deque

os.nice(19)  # Set process priority to maximum (Linux only)

def clear_console():
    """Fungsi clear console yang lebih cepat"""
    print('\033c', end='')  # ANSI escape code lebih cepat daripada os.system

class UltraLowLatencyAudioMonitor:
    def __init__(self):
        # Konfigurasi Ultra-Low Latency
        self.SAMPLE_RATE = 48000  # Sample rate lebih tinggi untuk respon lebih cepat
        self.BLOCK_SIZE = 64     # Buffer sangat kecil untuk latency minimal
        self.volume_history = deque(maxlen=10)
        self.running = True
        
        # Setup audio dengan optimasi khusus
        try:
            self.loopback = sc.get_microphone(
                id=str(sc.default_speaker().name),
                include_loopback=True
            )
            print(f"⚡ Ultra-Low Latency Mode | Buffer: {self.BLOCK_SIZE} samples")
            print(f"🎧 Source: {sc.default_speaker().name}")
        except Exception as e:
            print(f"❌ Audio init error: {str(e)}")
            raise

    def calculate_volume(self, data):
        """Optimasi ekstrim: RMS dalam satu baris dengan pre-computed constants"""
        return 20 * np.log10(np.sqrt(np.dot(data, data)/len(data)) + 1e-10)

    def monitor_loop(self):
        try:
            with self.loopback.recorder(
                samplerate=self.SAMPLE_RATE,
                blocksize=self.BLOCK_SIZE
            ) as mic:
                
                # Warm-up buffer
                mic.record(numframes=self.BLOCK_SIZE)
                
                # Variabel tracking performa
                last_time = time.perf_counter()  # Lebih presisi dari time.time()
                fps_counter = 0
                fps = 0
                
                while self.running:
                    # 1. Ambil data audio (BLOCK_SIZE samples)
                    data = mic.record(numframes=self.BLOCK_SIZE)
                    
                    # 2. Konversi ke mono secara ultra-cepat
                    data = data.mean(axis=1) if data.ndim > 1 else data
                    
                    # 3. Hitung volume (optimasi assembly-level numpy)
                    vol_db = 20 * np.log10(np.sqrt(np.mean(np.square(data)))) + 1e-10
                    self.volume_history.append(vol_db)
                    
                    # 4. Update FPS counter setiap 10 frame
                    fps_counter += 1
                    if fps_counter % 10 == 0:
                        fps = 10 / (time.perf_counter() - last_time)
                        last_time = time.perf_counter()
                    
                    # 5. Tampilan real-time (minimal overhead)
                    print(
                        f"\033[2J\033[H"  # Clear screen cepat dengan ANSI
                        f"⚡ VOL: {vol_db:6.1f} dB | "
                        f"FPS: {fps:5.1f} | "
                        f"Buf: {self.BLOCK_SIZE} samples\n"
                        f"{'█' * int(np.clip((vol_db+60)/1.2, 0, 50)):<50}"
                    )
                    
                    # 6. Adjust sleep time secara dinamis
                    time.sleep(max(0, 0.0001))  # Hampir no delay

        except KeyboardInterrupt:
            print("\n🛑 Stopped by user")
        except Exception as e:
            print(f"\n⚠️ Critical error: {str(e)}")

if __name__ == "__main__":
    print("🔥 Starting Ultra-Low Latency Audio Monitor...")
    monitor = UltraLowLatencyAudioMonitor()
    monitor.monitor_loop()
