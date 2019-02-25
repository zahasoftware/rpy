namespace rnet.lib
{
    public interface ISwitch
    {
        ISwitch this[int pin] { get; }
        void Write(bool value);
    }
}
