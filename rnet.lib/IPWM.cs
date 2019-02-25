namespace rnet.lib
{
    public interface IPWM
    {
        IPWM this[int pin] { get; }
        void Write(int value);
        void Write(int value, int frequency);
    }
}
