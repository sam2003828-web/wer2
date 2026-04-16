import numpy as np
import matplotlib.pyplot as plt

# 建立時間軸
t = np.linspace(0, 1, 500, endpoint=False)

# 乾淨訊號：5 Hz + 20 Hz
signal_clean = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 20 * t)

# 加入雜訊
noise = 0.8 * np.random.randn(len(t))
signal_noisy = signal_clean + noise

# FFT
fft_result = np.fft.fft(signal_noisy)
freq = np.fft.fftfreq(len(t), d=t[1] - t[0])

# 只取正頻率
mask = freq >= 0
freq_positive = freq[mask]
fft_positive = np.abs(fft_result[mask])

# 時間域圖
plt.figure()
plt.plot(t, signal_noisy)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Noisy Signal in Time Domain")
plt.show()

# 頻率域圖
plt.figure()
plt.plot(freq_positive, fft_positive)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("FFT Spectrum of Noisy Signal")
plt.show()